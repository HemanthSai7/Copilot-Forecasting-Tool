# Copilot-Forecasting-Tool
Project Submission for Copilot hackathon

### Installation

```bash
pip install -r requirements.txt
```

### Arguments

```bash
--city <city_name> # City name
--api-key <your openweathermap api key> # Openweathermap api key
--azure_sub_key <your azure subscription key> # Azure subscription key
--azure_lang_key <your azure language key> # Azure language key
--listen <Yes/No> # Listen for voice input
--prompt <Your text prompt> # Natural language prompt
```
- Please note that the `--api-key` ,`--azure_sub_key`,`--azure_lang_key`, `--listen` and `--prompt` arguments are optional. If not specified, the program will just use the default values.

- Type `python weather.py --help` for more information.

### Usage

```bash
python weather.py --city <city_name> --api-key <your openweathermap api key> --azure_sub_key <your azure subscription key> --azure_lang_key <your azure language key> --listen <Yes/No> --prompt <Your text prompt>
``` 

## Tech Stack
Microsoft Azure, OpenWeatherMap API, Python, SpeechRecognition, Requests, Time, OS, Math, Random, Pyinstaller


## How to get your Open API Keys for Azure and OpenWeatherMap
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Azure](https://azure.microsoft.com/en-us/)
