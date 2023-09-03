from pprint import pprint

import requests

from models.vacancy import Vacancy
from parsers.parser import APIParser


class HeadHunterParser(APIParser):
    def __init__(self):
        self.api_url = "https://api.hh.ru/"
        self.user_agent = "VacancyHelperApp/0.1"
        self.host = "hh.ru"
        self.search_params = {}

    def _get_page_data(self, query: str, page: int) -> dict:
        headers = {"HH-User-Agent": self.user_agent}
        url = self.api_url + "vacancies"
        params = {
            "text": query,  # text передается аргументом в get-запрос
            "host": self.host,
            "page": page,
            "per_page": 100,
            "period": 7,
            # "schedule": "remote",
            "only_with_salary": True,
        }
        response = requests.get(url=url, headers=headers, params=params)
        return response.json()

    @classmethod
    def vacancy_dict_to_object(cls, raw_vacancy: dict) -> Vacancy:

        vacancy = Vacancy(
            id=raw_vacancy["id"],
            name=raw_vacancy["name"],
            salary_from=raw_vacancy["salary"]["from"],
            salary_to=raw_vacancy["salary"]["to"],
            currency=raw_vacancy["salary"]["currency"],
            area=raw_vacancy["area"]["name"] if raw_vacancy["area"] else None,
            full_address=raw_vacancy["address"]["raw"]
            if raw_vacancy["address"]
            else None,
            url=raw_vacancy["alternate_url"],
            requirements=raw_vacancy["snippet"]["requirement"],
            employer=raw_vacancy["employer"]["name"],
        )
        return vacancy

    @classmethod
    def vacancies_to_objects(cls, raw_vacancies_list: list[dict]) -> list[Vacancy]:
        vacancy_obj_list = []
        for data in raw_vacancies_list:
            vacancy_obj_list.append(cls.vacancy_dict_to_object(data))
        return vacancy_obj_list

    def _get_raw_vacancies(self, query: str) -> list[dict]:
        first_page = self._get_page_data(query, 0)

        items: list = first_page["items"]

        total_pages = first_page["pages"]

        if total_pages > 1:
            for page in range(1, total_pages):
                page_items = self._get_page_data(query, page)["items"]
                items.extend(page_items)
        return items

    def get_vacancies(self, query) -> list[Vacancy]:

        items = self._get_raw_vacancies(query)

        objects_list = self.vacancies_to_objects(items)

        return objects_list

