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
        requirements="Тестовый текст обязанностей в вакансии",
        employer="Тестовый работодатель",
    )
    return vacancy
