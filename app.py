# Import the necessary modules
import requests
import azure.cognitiveservices.speech as speechsdk

# Define a Weather class
class Weather:
    # Define the __init__ method, which is called when a new instance of the class is created
    def __init__(self, city, api_key, azure_sub_key):
        # Store the city, API key, and Azure subscription key as instance variables
        self.city = city
        self.api_key = api_key
        self.azure_sub_key = azure_sub_key

    # Define a method to get the weather for the specified city
    def get_weather(self):
        # Construct the URL for the OpenWeatherMap API call
        url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric'
        # Send a GET request to the API and store the response
        response = requests.get(url)
        # Parse the response as JSON and extract the relevant weather data
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        # Return the weather data as a dictionary
        return weather
    
    # Define a method to speak the weather for the specified city
    def speak_weather(self, city, weather):
        # Create a SpeechConfig object with the Azure subscription key and region
        speech_config = speechsdk.SpeechConfig(subscription=self.azure_sub_key, region="centralindia")
        # Create a SpeechSynthesizer object with the SpeechConfig
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        
        # Construct a string with the weather information
        text = f"The current weather in {city} is {weather['description']}. The temperature is {weather['temperature']} degrees Celsius, with a humidity of {weather['humidity']} percent."
        # Call the SpeechSynthesizer's speak_text_async method with the weather string
        result = synthesizer.speak_text_async(text).get()
        
        # If the speech synthesis is successful, return the audio stream
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            audio_stream = result.audio_data_stream
            return audio_stream
        # Otherwise, return None
        else:
            return None