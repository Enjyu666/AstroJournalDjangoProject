from django.urls import path, include
from planner import views

app_name = 'planner'

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('add/<int:year>/<int:month>/<int:day>/', views.create_target, name='create_target')
]