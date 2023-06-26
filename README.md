# Copilot-Forecasting-Tool

**Copilot-Forecasting-Tool** is a weather forecasting tool that uses the OpenWeatherMap API to get the weather forecast for a given city. It also uses Microsoft Azure's Text to Speech API to convert text to speech. This tool can be used to get the weather forecast for any city in the world. It can also be used to get the weather forecast for the current location of the user. This tool can be used by anyone who wants to get the weather forecast for a given city.

## Installation
> Download zip or Clone the repository and run the following command in the terminal to install the required packages.

```bash
$ git clone https://github.com/HemanthSai7/Copilot-Forecasting-Tool
$ cd Copilot-Forecasting-Tool
$ pip install -r requirements.txt
```

## Arguments

```bash
--city <city_name> # City name
--api-key <your openweathermap api key> # Openweathermap api key
--azure_sub_key <your azure subscription key> # Azure subscription key
--azure_lang_key <your azure language key> # Azure language key
--listen <Yes/No> # Listen for voice input
--prompt <Your text prompt> # Natural language prompt
```
> -  Please note that the `--listen` and `--prompt` arguments are optional. 
> - If you want to use the voice input feature, you need to provide the `--listen` argument with a value of `Yes`.
> - If you want to use the `--prompt` argument with a natural language prompt. 
> - For both `--listen` and `--prompt` features, you need to provide the `--azure_sub_key` and `--azure_lang_key` arguments with your azure subscription key and azure language key respectively else it will use the default values.
> - Type `python weather.py --help` for more information.

## Usage
> In the terminal run the following command to get the weather forecast for the city of your choice.

```bash
python weather.py --city <city_name> --api-key <your openweathermap api key> --azure_sub_key <your azure subscription key> --azure_lang_key <your azure language key> --listen <Yes/No> --prompt <Your text prompt>
``` 

## Usage of Github Copilot in the project
- **API Integration :** *GitHub Copilot* helped us to quickly and easily generate the code to make API requests to the OpenWeatherMap API. This saved us a lot of time and effort, as we didn't have to manually write the code ourselves.
- **Data Parsing :** *GitHub Copilot* helped us to parse the JSON response from the API and extract the relevant weather information. This was a complex task, but GitHub Copilot was able to do it quickly and accurately.
- **Error Handling :** *GitHub Copilot* helped us to write code that would handle errors gracefully. This is important, as errors can occur when making API requests or parsing JSON data. GitHub Copilot was able to help us to write code that would handle these errors in a way that was both informative and user-friendly.
- **Documentation :** *GitHub Copilot* helped us to write documentation for our code. This is important, as it allows other developers to understand what our code does and how it works. GitHub Copilot was able to help us to write documentation that was both informative and easy to understand.

## Tech Stack
> **Microsoft Azure, OpenWeatherMap API, Python, SpeechRecognition, Requests, Time, OS, Math, Random, Pyinstaller**

## How to get your Open API Keys for Microsoft Azure and OpenWeatherMap
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Microsoft Azure](https://azure.microsoft.com/en-us/)


## Team Members
| Name | Github |
| --- | --- |
| Vishesh Tripathi | [Vishesh Tripathi](https://github.com/Vishesht27) |
| Mayuresh Agashe | [Mayuresh Agashe](https://github.com/mayureshagashe2105) |
| Hemanth Sai Garladinne | [Hemanth Sai Garladinne](https://github.com/HemanthSai7) |

