from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views import View

from objects.forms import CreateObjectForm, BaseObjectForm, EditObjectForm, DeleteObjectForm
from objects.models import CelestialObject


# def object_list(request):
#     objects = CelestialObject.objects.all().order_by('name')
#
#     context = {
#         'objects': objects,
#     }
#
#     return render(request, 'objects/object_list.html', context)

class ObjectListView(ListView):
    model = CelestialObject
    template_name = 'objects/object_list.html'
    context_object_name = 'objects'
    # permission_required = 'objects.view_celestialobject'
    # queryset = CelestialObject.objects.all().order_by('name')

    def get_queryset(self):
        objects = CelestialObject.objects.all()
        object_type = self.request.GET.get('type')
        search_query = self.request.GET.get('q')

        if object_type:
            objects = objects.filter(object_type=object_type)

        if search_query:
            objects.filter(name__icontains=search_query)

        return objects.order_by('name')


# def object_create(request):
#     form = CreateObjectForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('objects:object_list')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'objects/object_form.html', context)

class ObjectCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CelestialObject
    form_class = CreateObjectForm
    template_name = 'objects/object_form.html'
    permission_required = 'objects.add_celestialobject'
    success_url = reverse_lazy('objects:object_list')


# def object_detail(request, pk):
#     object = get_object_or_404(CelestialObject.objects.filter(pk=pk))
#
#     context = {
#         'object': object
#     }
#
#     return render(request, 'objects/object_detail.html', context)

class ObjectDetailView(DetailView):
    model = CelestialObject
    template_name = 'objects/object_detail.html'
    context_object_name = 'objects'
    # permission_required = 'objects.view_celestialobject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['is_favourite'] = self.request.user.profile.favourite_objects.filter(
                pk=self.object.pk
            ).exists()
        else:
            context['is_favourite'] = False

        return context



# def object_edit(request, pk):
#     object = get_object_or_404(CelestialObject, pk=pk)
#     form = EditObjectForm(request.POST or None, request.FILES or None, instance=object)
#
#     if form.is_valid():
#         form.save()
#         return redirect('objects:object_list')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'objects/object_form.html', context)

class ObjectEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CelestialObject
    form_class = EditObjectForm
    template_name = 'objects/object_form.html'
    permission_required = 'objects.change_celestialobject'
    success_url = reverse_lazy('objects:object_list')


# def object_delete(request, pk):
#     object = get_object_or_404(CelestialObject, pk=pk)
#     form = DeleteObjectForm(instance=object)
#
#     if request.method == 'POST':
#         object.delete()
#         return redirect('objects:object_list')
#
#     context = {
#         'form': form,
#         'object': object
#     }
#
#     return render(request, 'objects/object_confirm_delete.html', context)

class ObjectDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CelestialObject
    template_name = 'objects/object_confirm_delete.html'
    context_object_name = 'object'
    permission_required = 'objects.delete_celestialobject'
    success_url = reverse_lazy('objects:object_list')



# def filter_object_by_type(request):
#     object_type = request.GET.get('type')
#
#     if object_type:
#         objects = CelestialObject.objects.filter(object_type=object_type).order_by('name')
#     else:
#         objects = CelestialObject.objects.all().order_by('name')
#
#     context = {
#         'objects': objects,
#         'selected_type': object_type
#     }
#
#     return render(request, 'objects/object_list.html', context)


class FavouriteObjectView(LoginRequiredMixin, View):

    def post(self, request, pk):
        celestial_object = get_object_or_404(CelestialObject, pk=pk)
        user_profile = request.user.profile

        if user_profile.favourite_objects.filter(pk=pk).exists():
            user_profile.favourite_objects.remove(celestial_object)
        else:
            user_profile.favourite_objects.add(celestial_object)

        return redirect('objects:details', pk=pk)



class FavouriteObjectsListView(LoginRequiredMixin, ListView):
    model = CelestialObject
    template_name = 'objects/favourite_objects.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return self.request.user.profile.favourite_objects.all().order_by('name')









































