import pytz
from datetime import datetime

import settings

# Set up locale variables
localized_timezone = pytz.timezone(settings.timezone)
dateformat = settings.dateformat

def get_localized_current_time() -> str:
    """
    Retrieves localized current time.
        Returns:
            (str): String representation of localized current time.
    """
    timezone = pytz.timezone(settings.timezone)
    return datetime.now().astimezone(timezone).strftime(settings.dateformat)

def get_utc_datetime(utc_timestamp: str) -> datetime:
    """
    Generates a UTC datetime object from a UTC timestamp.
        Parameters:
            utc_timestamp (str): Timestamp representing UTC time.
        Returns:
            (datetime): The UTC datetime object based on the provided timestamp.
    """
    return datetime.fromtimestamp(utc_timestamp, pytz.utc)

def get_localized_datetime(utc_timestamp: str) -> datetime:
    """
    Generates a localized datetime object from the provided UTC timestamp.
        Parameters:
            utc_timestamp (str): Timestamp representing UTC time.
        Returns:
            (datetime): Localized datetime object based on the provided timestamp.
    """
    return get_utc_datetime(utc_timestamp).astimezone(localized_timezone)