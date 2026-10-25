from django import forms

from ExamProject.mixins import DisabledFieldsMixin
from equipment.models import Equipment


class BaseEquipmentForm(forms.ModelForm):

    def save(self, commit=True):
        equipment = super().save(commit=False)
        equipment.name = equipment.name.capitalize()

        if commit:
            equipment.save()

        return equipment

    class Meta:
        model = Equipment
        fields = '__all__'


class CreateEquipmentForm(BaseEquipmentForm):

    class Meta(BaseEquipmentForm.Meta):
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. My first telescope'
            }),
            'brand': forms.TextInput(attrs={
                'placeholder': 'e.g. Levenhuk (Optional)'
            }),
            'equipment_specs': forms.TextInput(attrs={
                'placeholder': 'e.g. 70x700 AZ (Optional)'
            }),
            'accessories': forms.TextInput(attrs={
                'placeholder': 'e.g. 12.5mm Eyepiece (Optional)'
            }),
        }
        error_messages = {
            'name': {
                'required': 'Please enter equipment name.',
            },
            'equipment_type': {
                'required': 'Please select equipment type.',
            }
        }


class EditEquipmentForm(BaseEquipmentForm):
    ...


class DeleteEquipmentForm(DisabledFieldsMixin, BaseEquipmentForm):
    ...