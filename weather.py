# Import the necessary modules
import os
import argparse
from app import Weather
from dotenv import load_dotenv
import scipy.io.wavfile

# Load environment variables from .env file
load_dotenv()

# Define the main function
def main():
    # Create an ArgumentParser object with a description of the program
    parser = argparse.ArgumentParser(description='Weather Application')
    # Add command-line arguments for the city name, API key, Azure subscription key, and voice output flag
    parser.add_argument('--city', '-c', help='City name')
    parser.add_argument('--api-key', '-KEY', help='API key for OpenWeatherMap')
    parser.add_argument('--azure-speech-key', help='API key for Azure Speech Service')
    parser.add_argument('--azure-lang-key', help='API key for Azure Language Service')
    parser.add_argument('--listen', '-v', help='Flag to enable voice output')
    parser.add_argument('--prompt', '-p', help='Flag to enable natural language prompt to get weather information')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the API key from the command-line arguments or environment variable
    api_key = args.api_key or os.getenv('API_KEY')
    # Get the Azure subscription key from the command-line arguments or environment variable
    azure_sub_key = args.azure_speech_key or os.getenv('AZURE_SUB_KEY')

    azure_lang_key = args.azure_lang_key or os.getenv('AZURE_LANGUAGE_KEY')

    # Check if the API key is missing
    if not api_key:
        print("API key is missing. Please provide the API key as an argument or set it in the environment variable (API_KEY).")
        return
    
    # Check if the Azure subscription key is missing
    if not azure_sub_key:
        print("Azure subscription key is missing. Please provide the key as an argument or set it in the environment variable (AZURE_SUB_KEY).")
        return
    
    if not azure_lang_key:
        print("Azure Language key is missing. Please provide the key as an argument or set it in the environment variable (AZURE_LANGUAGE_KEY).")
        return
    
    # Create a Weather object with the city name, API key, and Azure subscription key
    weather_app = Weather(args.city, api_key, azure_sub_key,azure_lang_key)

    # Get the weather data for the specified city
    weather = weather_app.get_weather()

    if args.city:
        print(f"Weather in {args.city}:")
        print(f"Country: {weather['country']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description']}")
        print(f"Wind Speed: {weather['wind_speed']} km/h")
        print(f"Time Zone: {weather['datetime']} GMT")
        print(f"Temperature feels like: {weather['feels_like']}°C")

    # Check if the voice output flag is set to "Yes"
    if args.listen == "Yes":
        # Generate the weather forecast audio and save it to a file
        audio_stream = weather_app.speak_weather(args.city, weather)
        if audio_stream:
            audio_file = "weather_forecast.wav"
            with open(audio_file, "wb") as file:
                scipy.io.wavfile.write(file, rate=44100, data=audio_stream)
    
            print("Weather forecast audio generated and saved as weather_forecast.wav.")
        else:
            print("Failed to generate weather forecast audio.")

            # Print the weather data to the console
            print(f"Weather in {args.city}:")
            print(f"Country: {weather['country']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Description: {weather['description']}")
            print(f"Wind Speed: {weather['wind_speed']} km/h")
            print(f"Time Zone: {weather['datetime']} GMT")
            print(f"Temperature feels like: {weather['feels_like']}°C")

    elif args.listen == "No":
        # Print the weather data to the console
        print(f"Weather in {args.city}:")
        print(f"Country: {weather['country']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description']}")
        print(f"Wind Speed: {weather['wind_speed']} km/h")
        print(f"Time Zone: {weather['datetime']} GMT")
        print(f"Temperature feels like: {weather['feels_like']}°C")



    if args.prompt:
        # Prompt the user to ask for weather information
        location,category=weather_app.entity_recognition(args.prompt)

        if category=="Location":
            # Print the weather data to the console
            print(f"Weather in {location}:")
            print(f"Country: {weather['country']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Description: {weather['description']}")
            print(f"Wind Speed: {weather['wind_speed']} km/h")
            print(f"Time Zone: {weather['datetime']} GMT")
            print(f"Temperature feels like: {weather['feels_like']}°C")


        else:
            print("Please provide a valid prompt")


# Call the main function if this script is being run directly
if __name__ == '__main__':
    main()