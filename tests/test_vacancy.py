import pytest

from models.vacancy import Vacancy
from exceptions.vacancy_exceptions import InvalidCSVRow, InvalidJSONData


def test_init(some_vacancy):
    """Базовая проверка инициализации"""
    assert some_vacancy.id == 1
    assert some_vacancy.name == "Тестовая вакансия"
    assert some_vacancy.salary_from == 100_000
    assert some_vacancy.salary_to == 150_000
    assert some_vacancy.currency == "RUB"
    assert some_vacancy.area == "Тестовый город"
    assert some_vacancy.full_address == "Г.Тестовый, ул Тестовая, 1"
    assert some_vacancy.url == "https://test.ru"
    assert some_vacancy.requirements == "Тестовый текст обязанностей в вакансии"
    assert some_vacancy.employer == "Тестовый работодатель"


def test_to_list(some_vacancy):
    """Проверка метода конвертации в список"""
    assert some_vacancy.to_list() == [
        1,
        "Тестовая вакансия",
        100_000,
        150_000,
        "RUB",
        "Тестовый город",
        "Г.Тестовый, ул Тестовая, 1",
        "https://test.ru",
        "Тестовый текст обязанностей в вакансии",
        "Тестовый работодатель",
    ]


def test_from_list():
    """Проверка инициализации из списка"""
    list_data_correct = [
        3,
        "Тестовая вакансия 3",
        100_000,
        150_000,
        "RUB",
        "Тестовый город",
        "Г.Тестовый, ул Тестовая, 1",
        "https://test.ru",
        "Тестовый текст обязанностей в вакансии",
        "Тестовый работодатель",
    ]
    vacancy_3 = Vacancy.from_list(list_data_correct)

    assert isinstance(vacancy_3, Vacancy)

    # Если количество полей не соответствует, возбуждается InvalidCSVRow
    with pytest.raises(InvalidCSVRow):
        list_data_incorrect = [
            "Тестовый работодатель",
        ]
        Vacancy.from_list(list_data_incorrect)


def test_to_dict(some_vacancy):
    """Проверка конвертации в словарь"""
    assert some_vacancy.to_dict() == {
        "id": 1,
        "name": "Тестовая вакансия",
        "salary_from": 100000,
        "salary_to": 150000,
        "currency": "RUB",
        "area": "Тестовый город",
        "full_address": "Г.Тестовый, ул Тестовая, 1",
        "url": "https://test.ru",
        "requirement": "Тестовый текст обязанностей в вакансии",
        "employer": "Тестовый работодатель",
    }


def test_from_dict():
    dict_data_correct = {
        "id": 4,
        "name": "Тестовая вакансия 4",
        "salary_from": 100000,
        "salary_to": 150000,
        "currency": "RUB",
        "area": "Тестовый город",
        "full_address": "Г.Тестовый, ул Тестовая, 1",
        "url": "https://test.ru",
        "requirement": "Тестовый текст обязанностей в вакансии",
        "employer": "Тестовый работодатель",
    }
    vacansy_4 = Vacancy.from_dict(dict_data_correct)
    assert isinstance(vacansy_4, Vacancy)

    with pytest.raises(InvalidJSONData):
        dict_data_incorrect = {
            "spam1": 4,
            "spam2": "Тестовая вакансия 4",
            "spam3": 100000,
            "spam4": 150000,
        }
        Vacancy.from_dict(dict_data_incorrect)


def test_short_requirements(some_vacancy):
    assert (
        some_vacancy.short_requirements == "Тестовый текст обязанностей в вакансии..."
    )


def test_to_print(some_vacancy):
    assert some_vacancy.to_print() == [
        "Тестовая вакансия",
        100000,
        150000,
        "RUB",
        "Тестовый город",
        "https://test.ru",
        "Тестовый текст обязанностей в вакансии...",
        "Тестовый работодатель",
    ]


def test_comparing(some_vacancy, some_vacancy_2):
    assert some_vacancy != some_vacancy_2
    assert some_vacancy < some_vacancy_2
    assert some_vacancy <= some_vacancy_2
    assert some_vacancy_2 >= some_vacancy
    assert some_vacancy_2 > some_vacancy
