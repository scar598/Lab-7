import unittest
from unittest.mock import patch

from hh.api.hh_api import Vacancy
from hh.presentation.display import HHVacancyDisplayer


class TestHHVacancyDisplayer(unittest.TestCase):
    def setUp(self):
        self.vacancies = [
            Vacancy(
                name='Python Dev',
                employer='Tech Company',
                salary='100000-150000 RUR',
                url='https://hh.ru/vacancy/123',
                published_at='2025-01-01'
            )
        ]

    @patch('builtins.print')
    def test_display_vacancies(self, mock_print):
        HHVacancyDisplayer.display_vacancies(self.vacancies)

        calls = mock_print.call_args_list

        outputs = [str(call_obj.args[0]) for call_obj in calls]
        combined_output = "\n".join(outputs)

        self.assertIn('Python Dev', combined_output)
        self.assertIn('Tech Company', combined_output)
        self.assertIn('100000-150000 RUR', combined_output)
        self.assertIn('https://hh.ru/vacancy/123', combined_output)
        self.assertIn('2025-01-01', combined_output)


if __name__ == '__main__':
    unittest.main()