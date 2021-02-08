from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('campgrounds/', views.pocketbook, name='pocketbook'),
    path('campgrounds/create', views.CampgroundCreate.as_view(), name='campgrounds_create'),
    path('campgrounds/<int:campground_id>', views.adventure_detail, name='detail'),
    path('campgrounds/<int:pk>/update/', views.CampgroundUpdate.as_view(), name='campground_update'),
    path('campgrounds/<int:pk>/delete/', views.CampgroundDelete.as_view(), name='campground_delete'),
    path('campgrounds/<int:campground_id>/add_trip/', views.add_trip, name='add_trip'),
    path('campgrounds/<int:pk>/update', views.TripUpdate.as_view(), name='trip_update'),
    path('trips/<int:pk>/delete', views.TripDelete.as_view(), name='trips_delete'),
    path('campgrounds/<int:campground_id>/add_photo', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]