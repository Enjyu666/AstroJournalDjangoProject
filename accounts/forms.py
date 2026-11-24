from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser, UserProfile


class CustomRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']


class UserProfileForm(forms.ModelForm):

    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'location', 'bio', 'profile_picture', 'is_public']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit = True):
        profile = super().save(commit=commit)

        profile.user.first_name = self.cleaned_data['first_name']
        profile.user.last_name = self.cleaned_data['last_name']
        profile.user.save()

        return profile