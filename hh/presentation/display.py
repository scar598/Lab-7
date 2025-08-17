from typing import List

from hh.api.hh_api import Vacancy

class HHVacancyDisplayer:
    @staticmethod
    def display_vacancies(vacancies: List[Vacancy]):
        print("\n🔍 Результаты поиска вакансий на hh.ru")
        print("=" * 60)

        for idx, vacancy in enumerate(vacancies, 1):
            print(f"\n🏆 Вакансия #{idx}")
            print(f"📌 Должность: {vacancy.name}")
            print(f"🏢 Компания: {vacancy.employer}")
            print(f"💰 Зарплата: {vacancy.salary}")
            print(f"🔗 Ссылка: {vacancy.url}")
            print(f"📅 Дата публикации: {vacancy.published_at}")
            print("-" * 50)

        print(f"\nНайдено вакансий: {len(vacancies)}")