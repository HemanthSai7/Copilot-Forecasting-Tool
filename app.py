import requests

import azure.cognitiveservices.speech as speechsdk

class Weather:
    def __init__(self, city, api_key,azure_sub_key):
        self.city = city
        self.api_key = api_key
        self.azure_sub_key=azure_sub_key

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
    
    def speak_weather(self,city, weather):
        speech_config = speechsdk.SpeechConfig(subscription=self.azure_sub_key, region="centralindia")
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        
        text = f"The current weather in {city} is {weather['description']}. The temperature is {weather['temperature']} degrees Celsius, with a humidity of {weather['humidity']} percent."
        result = synthesizer.speak_text_async(text).get()
        
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            audio_stream = result.audio_data_stream
            return audio_stream
        else:
            return None