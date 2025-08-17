import unittest
from unittest.mock import patch, Mock
import requests
from weather.api.weather_api import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_weather_data = {
            'name': 'Москва',
            'weather': [{'description': 'ясно'}],
            'main': {'temp': 20.5, 'humidity': 65, 'pressure': 1012},
            'wind': {'speed': 3.2}
        }
        cls.city = 'Москва'

    @patch('weather.api.weather_api.requests.get')
    def test_get_weather_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_weather_data
        mock_get.return_value = mock_response

        result = WeatherAPI.get_weather(self.city)
        assert result == self.sample_weather_data

        mock_get.assert_called_once()

    @patch('weather.api.weather_api.requests.get')
    def test_get_weather_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        result = WeatherAPI.get_weather(self.city)

        self.assertIsNone(result)
        mock_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
