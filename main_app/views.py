from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Campground
from .forms import TripForm
import requests
import os

api_key = os.environ['API_KEY']
parameters = {"api_key":api_key} 

def landing(request):
    all_campsites = {}
    if 'stateCode' in request.GET:
        statecode = request.GET['stateCode']
        endpoint = "https://developer.nps.gov/api/v1/campgrounds?stateCode=%s" %statecode
        response = requests.get(endpoint, params=parameters)
        data_all = response.json()
        spots = data_all['data']
        all_campsites = spots

        # for i in spots:
        #     if request.post:
        #         camp_data = Campsite(
        #             name = []
        #         )


    return render(request, 'landing.html', {'all_campsites': all_campsites})

def pocketbook(request):
    campgrounds = Campground.objects.all()
    return render(request, 'campgrounds/pocketbook.html', {'campgrounds': campgrounds})

def adventure_detail(request, campground_id):
    campground = Campground.objects.get(id=campground_id)
    trip_form = TripForm()
    return render(request, 'campgrounds/detail.html', {
        'campground': campground,
        'trip_form': trip_form
        })

def add_trip(request, campground_id):
    form = TripForm(request.POST)
    if form.is_valid():
        new_trip = form.save(commit=False)
        new_trip.campground_id = campground_id
        new_trip.save()
        return redirect('detail', campground_id=campground_id)

class CampgroundCreate(CreateView):
    model = Campground
    fields = '__all__'
    success_url = '/campgrounds/'


   