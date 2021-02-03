from django import forms
from django.conf import settings
import requests
import os
api_key = os.environ['API_KEY']
parameters = {"api_key":api_key} 

class CampgroundForm(forms.Form):
    state = forms.CharField(max_length=200)

    def search(self):
        # result = {}
        state = self.cleaned_data['stateCode']
        url = "https://developer.nps.gov/api/v1/campgrounds?"
        body = {
            'stateCode': state
        }
        response = requests.request(url, data=body ,params=parameters)
        print("response status code: " + str(response.status_code))
        data = response.json()
        spots = data['data']
        print(spots)

        return result


