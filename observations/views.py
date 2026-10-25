from django.shortcuts import render, redirect, get_object_or_404

from objects.models import CelestialObject
from observations.forms import CreateObservationForm, EditObservationForm, DeleteObservationForm
from observations.models import ObservationLog, ObservationImage


def observation_list(request):
    observations = ObservationLog.objects.all().order_by('-date_observed')

    context = {
        'observations': observations,
    }

    return render(request, 'observations/observation_list.html', context)


def observation_create(request, pk=None):
    initial = {}

    if pk is not None:
        celestial_object = get_object_or_404(CelestialObject, pk=pk)
        initial['celestial_object'] = celestial_object

    form = CreateObservationForm(request.POST or None, request.FILES or None, initial=initial)

    if form.is_valid():
        observation = form.save()

        for img in request.FILES.getlist('images'):
            ObservationImage.objects.create(observation=observation, image=img)

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
    form = EditObservationForm(request.POST or None, request.FILES or None, instance=observation)

    if form.is_valid():
        form.save()

        for img_pk in request.POST.getlist('delete_images'):
            photo = get_object_or_404(
                ObservationImage,
                pk=img_pk,
                observation=observation
            )
            photo.image.delete(save=False)
            photo.delete()

        for img in request.FILES.getlist('images'):
            ObservationImage.objects.create(observation=observation, image=img)

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


def gallery(request):
    images = ObservationImage.objects.select_related(
        'observation',
        'observation__celestial_object'
    ).order_by('-id')

    context = {
        'images': images
    }

    return render(request, 'observations/gallery.html', context)










