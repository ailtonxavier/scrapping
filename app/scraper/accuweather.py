import requests
from bs4 import BeautifulSoup
from typing import Optional
import re


def get_temperature(url: str, headers: dict) -> Optional[str]:
    """Fetches temperature text from an AccuWeather page.

    Returns just the temperature digits as a string (e.g., '30'), or None if not found.
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception:
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    
    temperature_text = None

    # Primary strategy: look for the current weather card
    current_weather_card = soup.find("div", class_="cur-con-weather-card__panel")
    if current_weather_card:
        temp_element = current_weather_card.find("div", class_="temp")
        if temp_element and temp_element.text:
            temperature_text = temp_element.text.strip()

    # Fallback: first generic .temp on the page
    if not temperature_text:
        generic_temp = soup.find("div", class_="temp")
        if generic_temp and generic_temp.text:
            temperature_text = generic_temp.text.strip()

    if temperature_text:
        # Extract only the digits from the string
        return re.sub(r"\D", "", temperature_text)

    return None
