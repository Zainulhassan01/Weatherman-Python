from django.shortcuts import render
import requests
from .models import City

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2422aa458f371a6f8d8e8b9a2d7a1af8'
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city.name)).json() #request the API data and convert the JSON to Python data types
        weather = {
            'city' : city.name,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'weather_data' : weather_data}
    return render(request, 'weatherapp/index.html', context)