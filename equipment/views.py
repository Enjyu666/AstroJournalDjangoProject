from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from equipment.forms import CreateEquipmentForm, EditEquipmentForm, DeleteEquipmentForm
from equipment.models import Equipment


# def equipment_list(request):
#     equipment = Equipment.objects.all().order_by('equipment_type')
#
#     context = {
#         'equipment': equipment
#     }
#
#     return render(request, 'equipment/equipment_list.html', context)

class EquipmentListView(ListView):
    model = Equipment
    template_name = 'equipment/equipment_list.html'
    context_object_name = 'equipment'
    queryset = Equipment.objects.all().order_by('equipment_type')
#
#
# def equipment_create(request):
#     form = CreateEquipmentForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('equipment:equipment_list')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'equipment/equipment_form.html', context)

class EquipmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Equipment
    form_class = CreateEquipmentForm
    template_name = 'equipment/equipment_form.html'
    permission_required = 'equipment.add_equipment'
    success_url = reverse_lazy('equipment:equipment_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




# def equipment_detail(request, pk):
#     equipment = get_object_or_404(Equipment.objects.filter(pk=pk))
#
#     context = {
#         'equipment': equipment
#     }
#
#     return render(request, 'equipment/equipment_detail.html', context)

class EquipmentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Equipment
    template_name = 'equipment/equipment_detail.html'
    context_object_name = 'equipment'
    permission_required = 'equipment.view_equipment'


# def equipment_edit(request, pk):
#     equipment = get_object_or_404(Equipment, pk=pk)
#     form = EditEquipmentForm(request.POST or None, instance=equipment)
#
#     if form.is_valid():
#         form.save()
#         return redirect('equipment:equipment_list')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'equipment/equipment_form.html', context)

class EquipmentEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Equipment
    form_class = EditEquipmentForm
    template_name = 'equipment/equipment_form.html'
    permission_required = 'equipment.change_equipment'
    success_url = reverse_lazy('equipment:equipment_list')


# def equipment_delete(request, pk):
#     equipment = get_object_or_404(Equipment, pk=pk)
#     form = DeleteEquipmentForm(instance=equipment)
#
#     if request.method == 'POST':
#         equipment.delete()
#         return redirect('equipment:equipment_list')
#
#     context = {
#         'form': form,
#         'equipment': equipment
#     }
#
#     return render(request, 'equipment/equipment_confirm_delete.html', context)

class EquipmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Equipment
    template_name = 'equipment/equipment_confirm_delete.html'
    context_object_name = 'equipment'
    permission_required = 'equipment.delete_equipment'
    success_url = reverse_lazy('equipment:equipment_list')



def filter_equipment_by_type(request):
    equipment_type = request.GET.get('type')

    if equipment_type:
        equipment = Equipment.objects.filter(equipment_type=equipment_type).order_by('equipment_type')
    else:
        equipment = Equipment.objects.all().order_by('equipment_type')

    context = {
        'equipment': equipment,
        'selected_type': equipment_type
    }

    return render(request, 'equipment/equipment_list.html', context)









