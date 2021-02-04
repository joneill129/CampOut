from django.urls import path
from . import views



urlpatterns = [
    path('', views.landing, name='landing'),
    path('campgrounds/', views.pocketbook, name='campgrounds_pocketbook')
]