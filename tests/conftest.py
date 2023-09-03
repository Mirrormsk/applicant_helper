import pytest
from models.vacancy import Vacancy


@pytest.fixture
def some_vacancy():
    vacancy = Vacancy(
        id=1,
        name="Тестовая вакансия",
        salary_from=100_000,
        salary_to=150_000,
        currency="rub",
        area="Тестовый город",
        full_address="Г.Тестовый, ул Тестовая, 1",
        url="https://test.ru",
        requirements="Тестовый текст обязанностей в <highlighttext>вакансии</highlighttext>",
        employer="Тестовый работодатель",
    )
    return vacancy

@pytest.fixture
def some_vacancy_2():
    vacancy = Vacancy(
        id=2,
        name="Тестовая вакансия",
        salary_from=140_000,
        salary_to=190_000,
        currency="rub",
        area="Тестовый город",
        full_address="Г.Тестовый, ул Тестовая, 2",
        url="https://test.ru",
        requirements="Тестовый текст обязанностей в <highlighttext>вакансии номер 2</highlighttext>",
        employer="Тестовый работодатель",
    )
    return vacancy
