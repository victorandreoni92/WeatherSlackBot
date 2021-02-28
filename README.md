## WeatherSlackBot

New England winters make for sad motorcycle riders. This AWS Lambda function fetches the local weather forecast for the next 7 days and checks whether there are any mild temperature riding days in the near future.
The forecast is sent to a Slack channel for easy consumption. 

![WeatherSlackBotScreenshot](https://victorandreoni.com/github/WeatherSlackBotScreenshot.PNG)

## Setup

All settings are located in the [`settings.py`](/bot/settings.py) file. 

The only required settings are the [`SLACK_TOKEN`](/bot/settings.py#L9) and [`OWM_TOKEN`](/bot/settings.py#L10) environment variables. The Slack token can be obtained from the [Slack API](https://api.slack.com/apps) portal.
The OWM token can be obtained from the [OpenWeatherMap API](https://openweathermap.org/api) portal.

The rest of the settings have default values, but should probably be modified since "mild temperature" can be subjective :slightly_smiling_face:
