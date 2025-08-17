import unittest
from unittest.mock import patch, Mock
import requests

from hh.api.hh_api import HHAPI, Vacancy

class TestHHAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_vacancy = {
            'name': 'Python Developer',
            'employer': {'name': 'Tech Company'},
            'salary': {'from': 100000, 'to': 150000, 'currency': 'RUR'},
            'alternate_url': 'https://hh.ru/vacancy/123',
            'published_at': '2025-01-01T12:00:00+0300'
        }

    @patch('hh.api.hh_api.requests.get')
    def test_get_vacancies_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': [self.sample_vacancy]}
        mock_get.return_value = mock_response

        result = HHAPI.get_vacancies()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Python Developer')
        mock_get.assert_called_once()

    @patch('hh.api.hh_api.requests.get')
    def test_get_vacancies_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        result = HHAPI.get_vacancies()
        self.assertIsNone(result)
        mock_get.assert_called_once()