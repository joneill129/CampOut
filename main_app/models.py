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
    classification = models.CharField(max_length=100)
    totalsites = models.CharField(max_length=10)
    cost = models.CharField(max_length=10)
    Image = models.ImageField()

    def __str__(self):
        return self.name

class Trip(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    classification = models.CharField(max_length=100)
    totalsites = models.CharField(max_length=10)
    cost = models.CharField(max_length=10)
    Image = models.ImageField()
    directions = models.URLField()

