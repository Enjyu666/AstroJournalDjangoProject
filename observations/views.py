from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from objects.models import CelestialObject
from observations.forms import CreateObservationForm, EditObservationForm, DeleteObservationForm
from observations.models import ObservationLog, ObservationImage


# def observation_list(request):
#     observations = ObservationLog.objects.all().order_by('-date_observed')
#     objects = CelestialObject.objects.order_by('name')
#
#     context = {
#         'observations': observations,
#         'objects': objects
#     }
#
#     return render(request, 'observations/observation_list.html', context)

class ObservationListView(ListView):
    model = ObservationLog
    template_name = 'observations/observation_list.html'
    context_object_name = 'observations'
    queryset = ObservationLog.objects.all().order_by('-date_observed')


# def observation_create(request, pk=None):
#     initial = {}
#
#     if pk is not None:
#         celestial_object = get_object_or_404(CelestialObject, pk=pk)
#         initial['celestial_object'] = celestial_object
#
#     form = CreateObservationForm(request.POST or None, request.FILES or None, initial=initial)
#
#     if form.is_valid():
#         observation = form.save()
#
#         for img in request.FILES.getlist('images'):
#             ObservationImage.objects.create(observation=observation, image=img)
#
#         return redirect('observations:observation_list')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'observations/observation_form.html', context)

class ObservationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ObservationLog
    form_class = CreateObservationForm
    template_name = 'observations/observation_form.html'
    permission_required = 'observation.add_observation'
    success_url = reverse_lazy('observations:observation_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#
# def observation_detail(request, pk):
#     observation = get_object_or_404(ObservationLog.objects.filter(pk=pk))
#
#     context = {
#         'observation': observation
#     }
#
#     return render(request, 'observations/observation_detail.html', context)

class ObservationDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = ObservationLog
    template_name = 'observations/observation_detail.html'
    context_object_name = 'observation'
    permission_required = 'observation.view_observation'


# def observation_edit(request, pk):
#     observation = get_object_or_404(ObservationLog, pk=pk)
#     form = EditObservationForm(request.POST or None, request.FILES or None, instance=observation)
#
#     if form.is_valid():
#         form.save()
#
#         for img_pk in request.POST.getlist('delete_images'):
#             photo = get_object_or_404(
#                 ObservationImage,
#                 pk=img_pk,
#                 observation=observation
#             )
#             photo.image.delete(save=False)
#             photo.delete()
#
#         for img in request.FILES.getlist('images'):
#             ObservationImage.objects.create(observation=observation, image=img)
#
#         return redirect('observations:observation_list')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'observations/observation_form.html', context)


class ObservationEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ObservationLog
    form_class = EditObservationForm
    template_name = 'observations/observation_form.html'
    permission_required = 'observation.change_observation'
    success_url = reverse_lazy('observations:observation_list')


# def observation_delete(request, pk):
#     observation = get_object_or_404(ObservationLog, pk=pk)
#     form = DeleteObservationForm(instance=observation)
#
#     if request.method == 'POST':
#         observation.delete()
#         return redirect('observations:observation_list')
#
#     context = {
#         'form': form,
#         'observation': observation
#     }
#
#     return render(request, 'observations/observation_confirm_delete.html', context)

class ObservationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ObservationLog
    template_name = 'observations/observation_confirm_delete.html'
    context_object_name = 'observation'
    permission_required = 'observation.delete_observation'
    success_url = reverse_lazy('observations:observation_list')


def gallery(request):
    images = ObservationImage.objects.select_related(
        'observation',
        'observation__celestial_object'
    ).order_by('-id')

    context = {
        'images': images
    }

    return render(request, 'observations/gallery.html', context)


def filter_observations_by_object(request):
    object = request.GET.get('object')

    if object:
        observations = ObservationLog.objects.filter(celestial_object_id=object).order_by('-date_observed')
    else:
        observations = ObservationLog.objects.all().order_by('-date_observed')

    objects = CelestialObject.objects.order_by('name')

    context = {
        'observations': observations,
        'objects': objects,
        'selected_object': object
    }

    return render(request, 'observations/observation_list.html', context)







