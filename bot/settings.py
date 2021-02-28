import os
import sys
from dotenv import load_dotenv

# Load dotenv environment variables
load_dotenv()

# Required variables
slack_token = os.getenv("SLACK_TOKEN")
owm_token = os.getenv("OWM_TOKEN")

# Exit if any of the required variables are missing
if slack_token is None or owm_token is None:
    sys.exit("Required variables are not set. Exiting.")

# Optional variables
slack_channel = os.getenv("SLACK_CHANNEL", "#chat")
slack_notification_text = os.getenv("SLACK_NOTIF_TEXT", "Weather forecast!")

zipcode = os.getenv("ZIPCODE", "02111")
timezone = os.getenv("TIMEZONE", "US/Eastern")
dateformat = os.getenv("DATEFORMAT", "%r %B %d, %Y")

min_good_temp = float(os.getenv("MIN_GOOD_TEMP", 50))
good_temp_emoji = os.getenv("GOOD_TEMP_EMOJI", ":tada:")
bad_temp_emoji = os.getenv("BAD_TEMP_EMOJI", ":cry:")

weather_unit = os.getenv("WEATHER_UNIT", "imperial")