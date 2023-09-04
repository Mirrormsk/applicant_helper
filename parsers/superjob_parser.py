import os
from pprint import pprint

import requests

from models.vacancy import Vacancy
from parsers.parser import APIParser

from utils.safe_request import get_request_safe

class SuperJobParser(APIParser):

    SJ_API_KEY = os.getenv("SJ_API_KEY")

    def __init__(self):
        self.host = "api.superjob.ru"
        self.api_url = "https://api.superjob.ru/2.0/vacancies/"

    def get_page_data(self, query, page):

        headers = {
            "Host": self.host,
            "X-Api-App-Id": self.SJ_API_KEY,
        }
        params = {
            "keyword": query,
            "period": 7,
            "page": page,
            "count": 100,
        }
        response = get_request_safe(self.api_url, headers=headers, params=params)
        return response.json()

    def _get_raw_vacancies(self, query):
        page = 0

        first_page = self.get_page_data(query, page)

        items: list = first_page["objects"]
        has_more = first_page["more"]

        while has_more:
            page += 1
            next_page = self.get_page_data(query, page)
            items.extend(next_page["objects"])
            has_more = next_page["more"]

        return items

    @classmethod
    def vacancy_dict_to_object(cls, raw_vacancy: dict) -> Vacancy:
        vacancy = Vacancy(
            id=raw_vacancy["id"],
            name=raw_vacancy["profession"],
            salary_from=raw_vacancy["payment_from"],
            salary_to=raw_vacancy["payment_to"],
            currency=raw_vacancy["currency"],
            area=raw_vacancy["client"]["town"]["title"]
            if "town" in raw_vacancy["client"].keys()
            else None,
            full_address=raw_vacancy["address"] if raw_vacancy["address"] else None,
            url=raw_vacancy["link"],
            requirements=raw_vacancy["candidat"].replace("\n", "") if raw_vacancy["candidat"] else None,
            employer=raw_vacancy["firm_name"],
        )
        return vacancy

    @classmethod
    def vacancies_to_objects(cls, raw_vacancies_list: list[dict]) -> list[Vacancy]:
        vacancy_obj_list = []
        for data in raw_vacancies_list:
            vacancy_obj_list.append(cls.vacancy_dict_to_object(data))
        return vacancy_obj_list

    def get_vacancies(self, query) -> list[Vacancy]:
        items = self._get_raw_vacancies(query)

        objects_list = self.vacancies_to_objects(items)

        return objects_list

