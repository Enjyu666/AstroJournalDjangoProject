from django import forms

from planner.models import ObservationTarget


class BaseObservationTargetForm(forms.ModelForm):

    class Meta:
        model = ObservationTarget
        exclude = ['user', 'scheduled_date']


class CreateObservationTargetForm(BaseObservationTargetForm):
    ...


class EditObservationTargetForm(BaseObservationTargetForm):
    ...