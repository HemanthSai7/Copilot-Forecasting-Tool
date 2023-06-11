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
--listen <Yes/No> # Listen for voice input
```
- Please note that the azure subscription key is optional. If you do not provide it, the program will not use the azure text to speech service.
- Type `python weather.py --help` for more information.

### Usage

```bash
python weather.py --city <city_name> --api-key <your openweathermap api key>
``` 
