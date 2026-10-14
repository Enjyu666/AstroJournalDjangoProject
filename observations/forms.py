from django import forms

from observations.models import ObservationLog


class BaseObservationForm(forms.ModelForm):

    class Meta:
        model = ObservationLog
        exclude = ['created_at']

        widgets = {
            'date_observed': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    'type': 'datetime-local',
                },
            ),
        }


class CreateObservationForm(BaseObservationForm):
    ...


class EditObservationForm(BaseObservationForm):
    ...


class DeleteObservationForm(BaseObservationForm):
    ...