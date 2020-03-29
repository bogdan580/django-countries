import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
from .forms import CountryForm
# Create your views here.

def hello(request):
    return HttpResponse("<h3>Welcome to home page</h3>")

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def index(request):
    url = 'https://restcountries.eu/rest/v2/name/{}'
    covid_url = 'https://covid-193.p.rapidapi.com/statistics?country={}'

    if(request.method == 'POST'):
        form = CountryForm(request.POST)
        form.save()

    form = CountryForm()

    countries = Country.objects.all()
    all_countries = []
    for country in countries:
        res = requests.get(url.format(country.name)).json()
        # print(url.format(country.name))
        headers = {'x-rapidapi-host': 'covid-193.p.rapidapi.com', 'x-rapidapi-key': '3e943f5da9mshf9baf8cb9f29560p120a78jsn9152f502a0df'}
        covid_res = requests.get(covid_url.format(country.name), headers = headers).json()
        # print(covid_url.format(country.name))
        countryInfo = {
            'country': res[0]['name'],
            'population': res[0]['population'],
            'total': covid_res['response'][0]['cases']['total'],
            'casesPercent': toFixed(covid_res['response'][0]['cases']['total'] * 100 / res[0]['population'], 5),
            'new': covid_res['response'][0]['cases']['new'],
        }
        all_countries.append(countryInfo)
    
    context = { 'all_info': all_countries, 'form': form }

    return render(request, 'home/index.html', context)   