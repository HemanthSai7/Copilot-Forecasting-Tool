import os
import requests
from dotenv import load_dotenv
load_dotenv()

# importing the required modules, Azure Speech SDK, Azure Text Analytics SDK and Azure Core Credentials
import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


# Define a Weather class
class Weather:
    # Define the __init__ method, which is called when a new instance of the class is created
    def __init__(self, city, api_key, azure_sub_key, azure_lang_key):
        # Store the city, API key, and Azure subscription key as instance variables
        self.city = city
        self.api_key = api_key
        self.azure_sub_key = azure_sub_key
        self.azure_lang_key = azure_lang_key

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
        

    def entity_recognition(self, text):
        # Get the Azure Language endpoint from the environment variables
        endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]

        # Create a TextAnalyticsClient object with the endpoint and Azure subscription key
        text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(self.azure_lang_key))

        # Create a list of reviews containing the specified text
        reviews = [f"""{text}"""]
        # Use the TextAnalyticsClient object to recognize entities in the reviews
        result = text_analytics_client.recognize_entities(reviews)
        # Filter out any errors in the result
        result = [review for review in result if not review.is_error]

        # Initialize variables for the location and category of the recognized entity
        location = None
        category = None
        # Loop through the result to find the first recognized entity
        for review in result:
            for entity in review.entities:
                # Set the location and category variables to the text and category of the entity
                location = entity.text
                category = entity.category
                # Break out of the loop after finding the first entity
                break

        # Return the location and category of the recognized entity
        return location, category