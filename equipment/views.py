from django.shortcuts import render, redirect, get_object_or_404

from equipment.forms import CreateEquipmentForm, EditEquipmentForm, DeleteEquipmentForm
from equipment.models import Equipment


def equipment_list(request):
    equipment = Equipment.objects.all().order_by('equipment_type')

    context = {
        'equipment': equipment
    }

    return render(request, 'equipment/equipment_list.html', context)


def equipment_create(request):
    form = CreateEquipmentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('equipment:equipment_list')

    context = {
        'form': form
    }

    return render(request, 'equipment/equipment_form.html', context)


def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment.objects.filter(pk=pk))

    context = {
        'equipment': equipment
    }

    return render(request, 'equipment/equipment_detail.html', context)


def equipment_edit(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    form = EditEquipmentForm(request.POST or None, instance=equipment)

    if form.is_valid():
        form.save()
        return redirect('equipment:equipment_list')

    context = {
        'form': form
    }

    return render(request, 'equipment/equipment_form.html', context)


def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    form = DeleteEquipmentForm(instance=equipment)

    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment:equipment_list')

    context = {
        'form': form,
        'equipment': equipment
    }

    return render(request, 'equipment/equipment_confirm_delete.html', context)













