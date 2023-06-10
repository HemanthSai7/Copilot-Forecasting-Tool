import os
from dotenv import load_dotenv
load_dotenv()
import requests

def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    weather = {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }
    return weather

if __name__ == '__main__':
    api_key = os.getenv('API_KEY')
    city = input('Enter a city name: ')
    weather = get_weather(city, api_key)
    print(f'Temperature: {weather["temperature"]}°C')
    print(f'Humidity: {weather["humidity"]}%')
    print(f'Description: {weather["description"]}')