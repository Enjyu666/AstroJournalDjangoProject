from django import forms

from ExamProject.mixins import DisabledFieldsMixin
from observations.models import ObservationLog


class BaseObservationForm(forms.ModelForm):

    class Meta:
        model = ObservationLog
        fields = '__all__'
        widgets = {
            'date_observed': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    'type': 'datetime-local',
                },
            ),
            'location': forms.TextInput(attrs={
                'placeholder': 'e.g. Plovdiv'
            }),

            'notes': forms.Textarea(attrs={
                'placeholder': 'e.g. Clear sky, good visibility',
            }),
            'rating': forms.RadioSelect(choices=[
                (5, '5 stars'),
                (4, '4 stars'),
                (3, '3 stars'),
                (2, '2 stars'),
                (1, '1 star')
            ]),

        }
        help_texts = {
            'equipment': 'Hold down Ctrl to select more than one piece of equipment used for this observation.',
        }
        error_messages = {
            'celestial_object': {
                'required': 'Please select an object.',
            },
            'object_type': {
                'required': 'Please select an object type.',
            },
            'date_observed': {
                'required': 'Please select a date.'
            },
            'equipment': {
                'required': 'Please select equipment.'
            }
        }



class CreateObservationForm(BaseObservationForm):
    ...


class EditObservationForm(BaseObservationForm):
    ...


class DeleteObservationForm(DisabledFieldsMixin, BaseObservationForm):

    class Meta(BaseObservationForm.Meta):

        exclude = ['rating', 'image']

