import os
import requests

from django.shortcuts import render
from dotenv  import load_dotenv

from .models import City, UserQuery
from .forms import CityForm
from .orm_query import user_query

load_dotenv()
WEATHER_KEY = os.environ.get('WEATHER_KEY')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    if request.method == 'POST':
        ip = get_client_ip(request)
        form = CityForm(request.POST)
        form.save()        
    
    form = CityForm()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+WEATHER_KEY
    cities = City.objects.all().order_by('-id')
    
    try:    
        response = requests.get(url.format(cities[0].name), params={'lang': 'ru'}).json()
        city_info = {
            'city': cities[0].name.capitalize(),
            'temp': response['main']['temp'],
            'wind': response['wind']['speed'],
            'weather': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        count =user_query(ip, cities[0].name.lower())
        
        context = {
            'info': city_info,
            'form': form, 
            'count': count
        }
        
        
        return render(request, 'weather/index.html', context)

    except:
        
        city_info = {
            'city': 'Извините, такого города нет',
            'temp': '-',
            'wind': '-',
            'weather': '-',
            'icon': '-',
        }
        context = {
            'info': city_info,
            'form': form
        }
        return render(request, 'weather/index.html', context)




