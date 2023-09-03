from models.vacancy import Vacancy


def test_vacancy(some_vacancy):
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
