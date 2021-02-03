from django.urls import path
from . import views



urlpatterns = [
    path('', views.landing, name='landing'),
    # path('campsites/', views.trips_index, name='trips_index')
]