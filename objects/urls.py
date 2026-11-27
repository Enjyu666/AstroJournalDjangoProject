from django.urls import path, include
from objects import views

app_name = 'objects'

urlpatterns = [
    path('', views.ObjectListView.as_view(), name='object_list'),
    path('create/' , views.ObjectCreateView.as_view(), name='create'),
    # path('filter/', views.filter_object_by_type, name='filter'),
    path('details/<int:pk>/', include([
        path('', views.ObjectDetailView.as_view(), name='details'),
        path('edit/', views.ObjectEditView.as_view(), name='edit'),
        path('delete/', views.ObjectDeleteView.as_view(), name='delete'),
        path('favourite/', views.FavouriteObjectView.as_view(), name='favourite')
    ])),
    path('favourites/', views.FavouriteObjectsListView.as_view(), name='favourites')
]