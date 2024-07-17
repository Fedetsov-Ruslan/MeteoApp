import os
import requests

from django.shortcuts import render
from dotenv  import load_dotenv

from .models import City
from .forms import CityForm

load_dotenv()
WEATHER_KEY = os.environ.get('WEATHER_KEY')

def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()        
    
    form = CityForm()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+WEATHER_KEY
    cities = City.objects.all().order_by('-id')
        
    response = requests.get(url.format(cities[0].name), params={'lang': 'ru'}).json()
    city_info = {
        'city': cities[0].name,
        'temp': response['main']['temp'],
        'wind': response['wind']['speed'],
        'weather': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }
    
    
    context = {
        'info': city_info,
        'form': form
    }
    return render(request, 'weather/index.html', context)


