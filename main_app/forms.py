from django.forms import ModelForm
from .models import Trip
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['startdate', 'enddate', 'reservation_link']
        widgets = {
            'startdate': DateInput(),
            'enddate': DateInput()
        }