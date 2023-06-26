# Copilot-Forecasting-Tool
Project Submission for Copilot hackathon

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
- 

## Tech Stack
**Microsoft Azure, OpenWeatherMap API, Python, SpeechRecognition, Requests, Time, OS, Math, Random, Pyinstaller**

## How to get your Open API Keys for Microsoft Azure and OpenWeatherMap
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Azure](https://azure.microsoft.com/en-us/)


## Team Members
| Name | Github |
| --- | --- |
| Vishesh Tripathi | [Vishesh Tripathi](https://github.com/Vishesht27) |
| Mayuresh Agashe | [Mayuresh Agashe](https://github.com/mayureshagashe2105) |
| Hemanth Sai Garladinne | [Hemanth Sai Garladinne](https://github.com/HemanthSai7) |

