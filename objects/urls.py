from django.urls import path, include
from objects import views

app_name = 'objects'

urlpatterns = [
    path('', views.object_list, name='object_list'),
    path('create/' , views.object_create, name='create'),
    path('details/<int:pk>/', include([
        path('', views.object_detail, name='details'),
        path('edit/', views.object_edit, name='edit'),
        path('delete/', views.object_delete, name='delete')
    ]))
]