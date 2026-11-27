import calendar
from datetime import date, timedelta
from multiprocessing import context
from pydoc import render_doc

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from objects.models import CelestialObject
from planner.forms import CreateObservationTargetForm, EditObservationTargetForm
from planner.models import ObservationTarget


@login_required()
def calendar_view(request):
    current_date = date.today()
    current_month = int(request.GET.get('month', current_date.month))
    current_year = int(request.GET.get('year', current_date.year))

    targets = ObservationTarget.objects.filter(
        user=request.user,
        scheduled_date__year=current_year,
        scheduled_date__month=current_month
    )

    month_calendar = calendar.monthcalendar(current_year, current_month)

    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    first_day_of_month = date(current_year, current_month, 1)
    previous_date = first_day_of_month - timedelta(days=1)
    previous_month = previous_date.month
    previous_year = previous_date.year

    last_day_of_month = date(
        current_year,
        current_month,
        calendar.monthrange(current_year, current_month)[1]
    )

    next_date = last_day_of_month + timedelta(days=1)
    next_month = next_date.month
    next_year = next_date.year

    celestial_objects = CelestialObject.objects.all()

    context = {
        'month_calendar': month_calendar,
        'current_month': current_month,
        'current_year': current_year,
        'month_name': calendar.month_name[current_month],
        'targets': targets,
        'weekdays': weekdays,
        'previous_month': previous_month,
        'previous_year': previous_year,
        'next_month': next_month,
        'next_year': next_year,
        'celestial_objects': celestial_objects
    }

    return render(request, 'planner/calendar.html', context)


@login_required()
def create_target(request, year, month, day):
    form = CreateObservationTargetForm(request.POST or None)
    target_date = date(year, month, day)

    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.instance.scheduled_date = target_date
        form.save()
        return redirect(f'/planner/?month={month}&year={year}')

    context = {
        'form': form,
        'target_date': target_date
    }

    return render(request, 'planner/create_target.html', context)


@login_required()
def edit_target(request, pk):
    target = get_object_or_404(
        ObservationTarget,
        pk=pk,
        user=request.user
    )
    form = EditObservationTargetForm(request.POST or None, instance=target)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(f'/planner/?month={target.scheduled_date.month}&year={target.scheduled_date.year}')


    context = {
        'form': form,
        'target': target
    }

    return render(request, 'planner/edit_target.html', context)


def delete_target(request, pk):
    target = get_object_or_404(
        ObservationTarget,
        pk=pk,
        user=request.user
    )

    target_date = target.scheduled_date

    if request.method == 'POST':
        target.delete()
        return redirect(f'/planner/?month={target_date.month}&year={target_date.year}')

    context = {
        'target': target
    }

    return render(request, 'planner/delete_target.html', context)



