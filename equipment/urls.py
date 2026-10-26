from django.urls import path, include
from . import views

app_name = 'equipment'

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('create/', views.equipment_create, name='create'),
    path('filter/', views.filter_equipment_by_type, name='filter'),
    path('details/<int:pk>/', include([
        path('', views.equipment_detail, name='details'),
        path('edit/', views.equipment_edit, name='edit'),
        path('delete/', views.equipment_delete, name='delete')
    ]))
]