from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Campground(models.Model):
    name = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    url = models.URLField
    
    def __str__(self):
        return self.name

class Trip(models.Model):
    date = models.DateField('Trip Date')
    directions = models.URLField()

