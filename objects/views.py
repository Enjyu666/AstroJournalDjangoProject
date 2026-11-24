from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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
    queryset = CelestialObject.objects.all().order_by('name')


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



def filter_object_by_type(request):
    object_type = request.GET.get('type')

    if object_type:
        objects = CelestialObject.objects.filter(object_type=object_type).order_by('name')
    else:
        objects = CelestialObject.objects.all().order_by('name')

    context = {
        'objects': objects,
        'selected_type': object_type
    }

    return render(request, 'objects/object_list.html', context)






















