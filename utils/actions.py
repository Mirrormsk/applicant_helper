from models.vacancy import Vacancy
from savers.saver import Saver


def sort_by_salary(vacancy: Vacancy):
    """Вспомогательная функция для сортировки по зарплате"""
    if vacancy.salary_to:
        return vacancy.salary_to
    return vacancy.salary_from


def has_words(vacancy: Vacancy, filter_words: list[str]):
    """Вспомогательная функция для фильтрации по ключевым словам"""
    vacancy_text = set(
        vacancy.name.lower().split() + vacancy.requirements.lower().split()
    )
    return set(filter_words) in vacancy_text


def sort_vacancies(vacancies: list[Vacancy], highest_first=True):
    """Функция для сортировки по зарплате.
    Сортирует по верхней границе. Если ее нет, то
    по нижней.
    """
    return sorted(vacancies, key=sort_by_salary, reverse=highest_first)


def filter_vacancies(vacancies: list[Vacancy], words_to_filter: list[str]):
    """Функция фильтрации вакансий по наличию ключевых слов"""
    filtered = []

    for vacancy in vacancies:
        if vacancy.requirements:
            if has_words(vacancy, words_to_filter):
                filtered.append(vacancy)

    return filtered


def filter_by_salary(saver: Saver):
    print(
        f"\nДля фильтрации во зарплате введите нижнюю и верхнюю границы. Поле можно оставить пустым."
    )

    # Поучение нижней границы
    salary_from = input("Введите нижнюю границу -> ")

    while salary_from and not salary_from.isdigit():
        salary_from = input("Введите нижнюю границу в числовом формате -> ")

    if salary_from:
        salary_from = int(salary_from)

    # Поучение верхней границы
    salary_to = input("Введите верхнюю границу -> ")

    while salary_to and not salary_to.isdigit():
        salary_to = input("Введите верхнюю границу в числовом формате -> ")

    if salary_to:
        salary_to = int(salary_to)

    result = saver.get_vacancies_by_salary(salary_from, salary_to)

    print(f"Получено {len(result)} вакансий подходящих под параметры")

    return result
