from models.vacancy import Vacancy
from savers.saver import Saver


def _sort_by_salary(vacancy: Vacancy):
    """Вспомогательная функция для сортировки по зарплате"""
    if vacancy.salary_to:
        return vacancy.salary_to
    return vacancy.salary_from


def has_words(vacancy: Vacancy, filter_words: list[str]):
    """Вспомогательная функция для фильтрации по ключевым словам"""

    # Разбиваем название и обязанности на отдельные слова и соединяем
    # в одно множество
    name = vacancy.name.lower().replace(",", " ").split()
    requirements = vacancy.requirements.lower().replace(",", " ").split()

    vacancy_text = set(name) | set(requirements)

    # Возвращаем является ли поисковая фраза подмножеством
    return set(filter_words) < vacancy_text


def sort_vacancies(vacancies: list[Vacancy], highest_first=True):
    """Функция для сортировки по зарплате.
    Сортирует по верхней границе. Если ее нет, то
    по нижней.
    """
    return sorted(vacancies, key=_sort_by_salary, reverse=highest_first)


def filter_by_keywords(vacancies: list[Vacancy], words_to_filter: list[str]):
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
    else:
        salary_from = 0

    # Поучение верхней границы
    salary_to = input("Введите верхнюю границу -> ")

    while salary_to and not salary_to.isdigit():
        salary_to = input("Введите верхнюю границу в числовом формате -> ")

    if salary_to:
        salary_to = int(salary_to)
    else:
        salary_to = float("inf")

    result = saver.get_vacancies_by_salary(salary_from, salary_to)

    print(f"Получено {len(result)} вакансий подходящих под параметры")

    return result
