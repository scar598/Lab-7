import requests
from typing import Dict, Optional, List
from dataclasses import dataclass

from hh.config.settings import settings


@dataclass
class Vacancy:
    name: str
    employer: str
    salary: Optional[str]
    url: str
    published_at: str


class HHAPI:
    @staticmethod
    def get_vacancies() -> Optional[List[Dict]]:
        try:
            params = {
                'text': settings.TEXT,
                'area': settings.AREA,
                'per_page': 10,
                'page': 1
            }
            response = requests.get(settings.BASE_URL, params=params)
            response.raise_for_status()
            return response.json().get('items', [])
        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def parse_vacancies(raw_data: List[Dict]) -> List[Vacancy]:
        vacancies = []
        for item in raw_data:
            salary = HHAPI._format_salary(item.get('salary'))
            vacancies.append(Vacancy(
                name=item.get('name', 'Без названия'),
                employer=item['employer']['name'],
                salary=salary,
                url=item['alternate_url'],
                published_at=item['published_at'][:10]  # YYYY-MM-DD
            ))
        return vacancies

    @staticmethod
    def _format_salary(salary_data: Optional[Dict]) -> str:
        if not salary_data:
            return "Не указана"

        components = []
        if salary_data.get('from'):
            components.append(f"от {salary_data['from']}")
        if salary_data.get('to'):
            components.append(f"до {salary_data['to']}")
        if salary_data.get('currency'):
            components.append(salary_data['currency'].upper())

        return ' '.join(components) if components else "Не указана"