from django.urls import path, include
from observations import views

app_name = 'observations'

urlpatterns = [
    path('', views.observation_list, name='observation_list'),
    path('create/', include([
        path('', views.observation_create, name='create'),
        path('from-object/<int:pk>/', views.observation_create, name='create_from_object')
    ])),
    path('details/<int:pk>/', include([
        path('', views.observation_detail, name='details'),
        path('edit/', views.observation_edit, name='edit'),
        path('delete/', views.observation_delete, name='delete')
    ])),
    path('gallery/', views.gallery, name='gallery'),
]