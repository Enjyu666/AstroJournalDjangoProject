from django import forms

from objects.models import CelestialObject


class BaseObjectForm(forms.ModelForm):


    class Meta:
        model = CelestialObject
        fields = '__all__'
        # error_messages = {
        #     'name': ['The object name cannot contain less than 2 characters']
        # }


class CreateObjectForm(BaseObjectForm):
    ...


class EditObjectForm(BaseObjectForm):
    ...


class DeleteObjectForm(BaseObjectForm):
    ...