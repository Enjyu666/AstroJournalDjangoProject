from django.urls import path, include
from . import views

app_name = 'equipment'

urlpatterns = [
    path('', views.EquipmentListView.as_view(), name='equipment_list'),
    path('create/', views.EquipmentCreateView.as_view(), name='create'),
    path('filter/', views.filter_equipment_by_type, name='filter'),
    path('details/<int:pk>/', include([
        path('', views.EquipmentDetailView.as_view(), name='details'),
        path('edit/', views.EquipmentEditView.as_view(), name='edit'),
        path('delete/', views.EquipmentDeleteView.as_view(), name='delete')
    ]))
]