
from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts.views import CreateUserView, DetailProfileView, EditProfileView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', include([
        path('edit/', EditProfileView.as_view(), name='edit_profile'),
        path('<str:username>/', DetailProfileView.as_view(), name='profile'),
    ])),
]