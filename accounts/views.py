from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse

from accounts.forms import CustomRegistrationForm, UserProfileForm
from accounts.models import UserProfile


class CreateUserView(CreateView):
    form_class = CustomRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class DetailProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        profile = get_object_or_404(UserProfile, user__username=self.kwargs['username'])
        if profile.is_public or profile.user == self.request.user:
            return profile

        raise Http404



class EditProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'accounts/edit_profile.html'

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user.username})