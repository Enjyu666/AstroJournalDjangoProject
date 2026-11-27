from django import forms

from planner.models import ObservationTarget


class BaseObservationTargetForm(forms.ModelForm):

    class Meta:
        model = ObservationTarget
        exclude = ['user']


class CreateObservationTargetForm(BaseObservationTargetForm):

    class Meta(BaseObservationTargetForm.Meta):
        exclude = ['user', 'scheduled_date']


class EditObservationTargetForm(BaseObservationTargetForm):
    ...