from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError 

import settings

def post_message(channel: str, text: str, blocks: list) -> bool:
    """
    Posts messages to slack.
        Parameters:
            channel (str): The channel to post the message to.
            text (str): The fallback text if the block content cannot be posted.
            blocks (list): The block content of the message.
        Returns:
            (bool): Whether posting the message was successful.
    """
    slack_web_client = WebClient(token=settings.slack_token)
    try:
        slack_web_client.chat_postMessage(channel= channel, text= text, blocks = blocks)
        return True
    except SlackApiError as e:
        print(e.response)
        return False 

def generate_forecast_message(forecast: dict, current_time: str) -> list:
    """
    Generates the formatted message for the weather forecast, using the Slack block message structure.
    https://api.slack.com/reference/block-kit/blocks
        Parameters:
            forecast (dict): The forecast information, with the key structure of date -> temperature
            current_time (str): The localized and formatted current time string.
        Returns:
            (list): The slack message.
    """
    blocks = []
    blocks.append(generate_header_block(current_time))
    for date, temp in forecast.items():
        blocks.append(generate_forecast_block(date, temp)) 

    return blocks

def generate_header_block(current_time: str) -> dict:
    """
    Generates the header block for the slack message.
        Parameters:
            current_time (str): The current time string.
        Returns:
            (dict of str: str): The header block.
    """
    block = {}
    block["type"] = "header"
    block["text"] = {}
    block["text"]["type"] = "plain_text"
    block["text"]["text"] = f'Weather forecast as of {current_time}!'
    return block

def generate_forecast_block(date: str, temp: float) -> dict:
    """
    Generates the forecast block for the slack message.
        Parameters:
            date (str): The date the forecast is for.
            temp (float): The temperature for the day.
        Returns:
            (dict of str: str) The forecast block.
    """
    block = {}
    block["type"] = "section"
    block["text"] = {}
    block["text"]["type"] = "mrkdwn"

    message = f"*Date:* {date}, *Temp:* {temp}{get_weather_unit_symbol(settings.weather_unit)}. "
    
    if temp > settings.min_good_temp:
        message += settings.good_temp_emoji * 3 # Repeat good emoji 3 times
    else:
        message += settings.bad_temp_emoji
    
    block["text"]["text"] = message
    return block

def get_weather_unit_symbol(weather_unit: str) -> str:
    """
    Generates the weather unit symbol based on the unit.
        Parameters:
            weather_unit (str): The weather unit to generate the symbol for.
        Returns:
            (str): The weather unit symbol.
    """
    if weather_unit == "imperial":
        return "°F"
    elif weather_unit == "metric":
        return "°C"
    else:
        return ""