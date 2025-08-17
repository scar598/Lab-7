import unittest
from unittest.mock import patch

from weather.presentation.display import ConsoleWeatherDisplayer


class TestConsoleWeatherDisplayer(unittest.TestCase):
    def setUp(self):
        self.weather_data = {
            'city': 'Москва',
            'description': 'ясно',
            'temperature': 20.5,
            'humidity': 65,
            'pressure': 1012,
            'wind_speed': 3.2
        }

    @patch('builtins.print')
    def test_display_weather(self, mock_print):
        ConsoleWeatherDisplayer.display_weather(self.weather_data)

        calls = mock_print.call_args_list

        outputs = [str(call.args[0]) for call in calls]
        combined_output = "\n".join(outputs)

        self.assertIn('Москва', combined_output)
        self.assertIn('Ясно', combined_output)
        self.assertIn('20.5°C', combined_output)
        self.assertIn('65%', combined_output)
        self.assertIn('1012 гПа', combined_output)
        self.assertIn('3.2 м/с', combined_output)

if __name__ == '__main__':
    unittest.main()
