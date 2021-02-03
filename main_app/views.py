from django.shortcuts import render, redirect


# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def trips_index(request):
    return render(request, 'pocketbook.html')