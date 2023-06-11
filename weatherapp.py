import os
import requests
import azure.cognitiveservices.speech as speechsdk
import argparse

from dotenv import load_dotenv
load_dotenv()

class Weather:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key

    def get_weather(self):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        return weather


def speak_weather(city, weather):
    speech_config = speechsdk.SpeechConfig(subscription="537be803-988c-4bdf-85b6-5027b562f13c", region="centralindia")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    
    text = f"The current weather in {city} is {weather['description']}. The temperature is {weather['temperature']} degrees Celsius, with a humidity of {weather['humidity']} percent."
    result = synthesizer.speak_text_async(text).get()
    
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        audio_stream = result.audio_data_stream
        return audio_stream
    else:
        return None
    
def main():
    parser = argparse.ArgumentParser(description='Weather Application')
    parser.add_argument('--city', '-c',help='City name')
    parser.add_argument('--api-key','-KEY',help='API key for OpenWeatherMap')

    args = parser.parse_args()

    api_key = args.api_key or os.getenv('API_KEY')

    if not api_key:
        print("API key is missing. Please provide the API key as an argument or set it in the environment variable (API_KEY).")
        return

    weather_app = Weather(args.city, api_key)

    weather = weather_app.get_weather()

    audio_stream = speak_weather(args.city, weather)
    

    print(f"Weather in {args.city}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Description: {weather['description']}")


    if audio_stream:
        audio_file = "weather_forecast.wav"
        with open(audio_file, "wb") as file:
            file.write(audio_stream.get_wav_data())

        print("Weather forecast audio generated and saved as weather_forecast.wav.")
    else:
        print("Failed to generate weather forecast audio.")

if __name__ == '__main__':
    main()    