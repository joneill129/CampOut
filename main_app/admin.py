from django.contrib import admin
from .models import Campground, Trip, Photo

# Register your models here.
admin.site.register(Campground)
admin.site.register(Trip)
admin.site.register(Photo)