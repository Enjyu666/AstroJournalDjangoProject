from django.urls import path, include
from observations import views

app_name = 'observations'

urlpatterns = [
    path('', views.ObservationListView.as_view(), name='observation_list'),
    path('gallery/', views.gallery, name='gallery'),
    path('filter/', views.filter_observations_by_object, name='filter'),
    path('create/', include([
        path('', views.ObservationCreateView.as_view(), name='create'),
        path('from-object/<int:pk>/', views.ObservationCreateView.as_view(), name='create_from_object')
    ])),
    path('details/<int:pk>/', include([
        path('', views.ObservationDetailView.as_view(), name='details'),
        path('edit/', views.ObservationEditView.as_view(), name='edit'),
        path('delete/', views.ObservationDeleteView.as_view(), name='delete')
    ])),
]