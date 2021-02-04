from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models

# Create your models here.

class Campground(models.Model):
    name = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    zipcode = models.CharField(max_length=15, default='')
    directions = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=15, default='')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'campground_id': self.id})

class Trip(models.Model):
    startdate = models.DateField('Start Date')
    enddate = models.DateField('End Date')

    campground = models.ForeignKey(Campground, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.date}"

   

