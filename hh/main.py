from hh.api.hh_api import HHAPI

from hh.presentation.display import HHVacancyDisplayer


def main():
    raw_data = HHAPI.get_vacancies()
    vacancies = HHAPI.parse_vacancies(raw_data)

    HHVacancyDisplayer.display_vacancies(vacancies)


if __name__ == "__main__":
    main()
