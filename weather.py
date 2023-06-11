import os
import argparse

from app import Weather

from dotenv import load_dotenv
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Weather Application')
    parser.add_argument('--city', '-c',help='City name')
    parser.add_argument('--api-key','-KEY',help='API key for OpenWeatherMap')
    parser.add_argument('--azure-sub-key',help='API key for Azure Speech Service')
    parser.add_argument('--listen','-v',help='Flag to enable voice output')

    args = parser.parse_args()

    api_key = args.api_key or os.getenv('API_KEY')
    azure_sub_key = args.azure_sub_key or os.getenv('AZURE_SUB_KEY')

    if not api_key:
        print("API key is missing. Please provide the API key as an argument or set it in the environment variable (API_KEY).")
        return
    
    if not azure_sub_key:
        print("Azure subscription key is missing. Please provide the key as an argument or set it in the environment variable (AZURE_SUB_KEY).")
        return
    
    weather_app = Weather(args.city, api_key,azure_sub_key)

    weather = weather_app.get_weather()

    print(f"Weather in {args.city}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Description: {weather['description']}")

    if args.listen:
        audio_stream = weather_app.speak_weather(args.city, weather)
        if audio_stream:
            audio_file = "weather_forecast.wav"
            with open(audio_file, "wb") as file:
                file.write(audio_stream.get_wav_data())
    
            print("Weather forecast audio generated and saved as weather_forecast.wav.")
        else:
            print("Failed to generate weather forecast audio.")

if __name__ == '__main__':
    main()    