from django.urls import path
from . import views



urlpatterns = [
    path('', views.landing, name='landing'),
    path('campgrounds/', views.pocketbook, name='campgrounds_pocketbook'),
    path('campgrounds/create', views.CampgroundCreate.as_view(), name='campgrounds_create'),
    path('campgrounds/<int:campground_id>', views.adventure_detail, name='detail'),
    path('campgrounds/<int:pk>/update/', views.CampgroundUpdate.as_view(), name='campground_update'),
    path('campgrounds/<int:campground_id>/add_trip/', views.add_trip, name='add_trip'),
    path('campgrounds/photos', views.add_photo, name='add_photo')
]