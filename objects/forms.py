from django import forms

from ExamProject.mixins import DisabledFieldsMixin
from objects.models import CelestialObject


class BaseObjectForm(forms.ModelForm):

    def save(self, commit=True):
        object = super().save(commit=False)
        object.name = object.name.capitalize()

        if commit:
            object.save()

        return object


    class Meta:
        model = CelestialObject
        fields = '__all__'



class CreateObjectForm(BaseObjectForm):

    class Meta(BaseObjectForm.Meta):
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Andromeda'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'e.g. Nearest galaxy to the Milky Way (Optional)'
            }),
        }
        error_messages = {
            'name': {
                'min_length': 'The object name must contain at least 2 characters.',
                'required': 'Please enter an object name.',
            },
            'object_type': {
                'required': 'Please select an object type.',
            },
        }


class EditObjectForm(BaseObjectForm):
    ...


class DeleteObjectForm(DisabledFieldsMixin, BaseObjectForm):

    class Meta(BaseObjectForm.Meta):
        exclude = ['image']