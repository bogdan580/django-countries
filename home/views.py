import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
# Create your views here.

def hello(request):
    return HttpResponse("<h3>Welcome to home page</h3>")

def index(request):
    url = 'https://restcountries.eu/rest/v2/name/{}'
    countries = Country.objects.all()
    all_countries = []
    for country in countries:
        res = requests.get(url.format(country.name)).json()
        print(url.format(country.name))
        countryInfo = {
            'country': res[0]['name'],
            'population': res[0]['population']
        }
        all_countries.append(countryInfo)
    
    context = { 'all_info': all_countries }

    return render(request, 'home/index.html', context)