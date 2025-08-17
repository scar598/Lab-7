import requests
from typing import Optional, Dict

from weather.config.settings import settings


class WeatherAPI:
    @staticmethod
    def get_weather(city: str) -> Optional[Dict]:
        try:
            params = {
                'q': city,
                'appid': settings.API_KEY,
                'units': settings.UNITS,
                'lang': settings.LANGUAGE
            }
            response = requests.get(settings.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def parse_weather_data(data: Dict) -> Dict:
        return {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }