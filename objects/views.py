from django.shortcuts import render, redirect, get_object_or_404

from objects.forms import CreateObjectForm, BaseObjectForm, EditObjectForm, DeleteObjectForm
from objects.models import CelestialObject


def object_list(request):
    objects = CelestialObject.objects.all().order_by('name')

    context = {
        'objects': objects,
    }

    return render(request, 'objects/object_list.html', context)


def object_create(request):
    form = CreateObjectForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('objects:object_list')

    context = {
        'form': form
    }

    return render(request, 'objects/object_form.html', context)


def object_detail(request, pk):
    object = get_object_or_404(CelestialObject.objects.filter(pk=pk))

    context = {
        'object': object
    }

    return render(request, 'objects/object_detail.html', context)


def object_edit(request, pk):
    object = get_object_or_404(CelestialObject, pk=pk)
    form = EditObjectForm(request.POST or None, request.FILES or None, instance=object)

    if form.is_valid():
        form.save()
        return redirect('objects:object_list')

    context = {
        'form': form
    }

    return render(request, 'objects/object_form.html', context)


def object_delete(request, pk):
    object = get_object_or_404(CelestialObject, pk=pk)
    form = DeleteObjectForm(instance=object)

    if request.method == 'POST':
        object.delete()
        return redirect('objects:object_list')

    context = {
        'form': form,
        'object': object
    }

    return render(request, 'objects/object_confirm_delete.html', context)



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






















