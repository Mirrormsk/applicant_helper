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

@pytest.fixture
def some_vacancy_3():
    vacancy = Vacancy(
        id=3,
        name="Тестовая вакансия",
        salary_from=140_000,
        salary_to=190_000,
        currency="rub",
        area="Тестовый город",
        full_address="Г.Тестовый, ул Тестовая, 2",
        url="https://test.ru",
        requirements="Тестовый текст обязанностей в <highlighttext>вакансии номер 3</highlighttext>",
        employer="Тестовый работодатель",
    )
    return vacancy


@pytest.fixture
def some_vacancy_without_salary_from():
    vacancy = Vacancy(
        id=4,
        name="Тестовая вакансия",
        salary_from=None,
        salary_to=190_000,
        currency="rub",
        area="Тестовый город",
        full_address="Г.Тестовый, ул Тестовая, 2",
        url="https://test.ru",
        requirements="Тестовый текст обязанностей в <highlighttext>вакансии номер 3</highlighttext>",
        employer="Тестовый работодатель",
    )
    return vacancy


@pytest.fixture
def some_vacancy_without_salary_to():
    vacancy = Vacancy(
        id=5,
        name="Тестовая вакансия",
        salary_from=140_000,
        salary_to=None,
        currency="rub",
        area="Тестовый город",
        full_address="Г.Тестовый, ул Тестовая, 2",
        url="https://test.ru",
        requirements="Тестовый текст обязанностей в <highlighttext>вакансии номер 3</highlighttext>",
        employer="Тестовый работодатель",
    )
    return vacancy


@pytest.fixture
def vacancy_python_php():
    vacancy = Vacancy(
        id=6,
        name="Тестовая вакансия python php",
        salary_from=100_000,
        salary_to=None,
        currency="rub",
        area="Тестовый город",
        full_address="Г.Тестовый, ул Тестовая, 2",
        url="https://test.ru",
        requirements="Python, php",
        employer="Тестовый работодатель",
    )
    return vacancy


@pytest.fixture
def vacancy_python_java_go():
    vacancy = Vacancy(
        id=7,
        name="Тестовая вакансия 10",
        salary_from=100_000,
        salary_to=None,
        currency="rub",
        area="Тестовый город",
        full_address="Г.Тестовый, ул Тестовая, 2",
        url="https://test.ru",
        requirements="Python, Java, Go",
        employer="Тестовый работодатель",
    )
    return vacancy

@pytest.fixture
def vacancy_python_java():
    vacancy = Vacancy(
        id=8,
        name="Тестовая вакансия 10",
        salary_from=100_000,
        salary_to=None,
        currency="rub",
        area="Тестовый город",
        full_address="Г.Тестовый, ул Тестовая, 2",
        url="https://test.ru",
        requirements="Python, Java",
        employer="Тестовый работодатель",
    )
    return vacancy