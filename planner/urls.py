from django.urls import path, include
from planner import views

app_name = 'planner'

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('add/<int:year>/<int:month>/<int:day>/', views.create_target, name='create_target'),
    path('edit/<int:pk>', views.edit_target, name='edit_target'),
    path('delete/<int:pk>/', views.delete_target, name='delete_target')
]