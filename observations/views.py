from django.shortcuts import render, redirect, get_object_or_404

from observations.forms import CreateObservationForm, EditObservationForm, DeleteObservationForm
from observations.models import ObservationLog


def observation_list(request):
    observations = ObservationLog.objects.all()

    context = {
        'observations': observations,
    }

    return render(request, 'observations/observation_list.html', context)


def observation_create(request):
    form = CreateObservationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('observations:observation_list')

    context = {
        'form': form
    }

    return render(request, 'observations/observation_form.html', context)


def observation_detail(request, pk):
    observation = get_object_or_404(ObservationLog.objects.filter(pk=pk))

    context = {
        'observation': observation
    }

    return render(request, 'observations/observation_detail.html', context)


def observation_edit(request, pk):
    observation = get_object_or_404(ObservationLog, pk=pk)
    form = EditObservationForm(request.POST or None, instance=observation)

    if form.is_valid():
        form.save()
        return redirect('observations:observation_list')

    context = {
        'form': form
    }

    return render(request, 'observations/observation_form.html', context)


def observation_delete(request, pk):
    observation = get_object_or_404(ObservationLog, pk=pk)
    form = DeleteObservationForm(instance=observation)

    if request.method == 'POST':
        observation.delete()
        return redirect('observations:observation_list')

    context = {
        'form': form,
        'observation': observation
    }

    return render(request, 'observations/observation_confirm_delete.html', context)

