import sys

import slack
import weather
import settings
import localizer

def handler(event, context):
    """
    Main function. Signature for AWS Lambda.
    """
    forecast = weather.get_daily_weather_forecast(settings.zipcode)
    if forecast is None:
        sys.exit("Could not retrieve weather forecast. Exiting.")
    
    slack_message = slack.generate_forecast_message(forecast, localizer.get_localized_current_time())
    if not (slack.post_message(channel= settings.slack_channel, text= settings.slack_notification_text, blocks= slack_message)):
        sys.exit("Could not post slack message. Exiting.")

if __name__ == "__main__":
    handler(None, None)