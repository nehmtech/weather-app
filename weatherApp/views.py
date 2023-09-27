from django.shortcuts import render
import requests
from .models import Weather
from django.conf import settings

def home(request):
    weather_data = None
    
    if request.method == 'POST':
        location = request.POST['location']
        api_key = settings.WEATHER_API_KEY
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric')
        
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity =data['main']['humidity']
            description = data['weather'][0]['description']
            
            weather = Weather.objects.create(
                location=location,
                temperature = temperature,
                humidity=humidity,
                description=description,                
            )
            
            weather.save()
            
    weather_data = Weather.objects.all()
        
    return render (request, 'weather.html', {'weather_data':weather_data})