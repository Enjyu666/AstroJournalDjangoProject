from django import forms

from equipment.models import Equipment


class BaseEquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'


class CreateEquipmentForm(BaseEquipmentForm):
    ...


class EditEquipmentForm(BaseEquipmentForm):
    ...


class DeleteEquipmentForm(BaseEquipmentForm):
    ...