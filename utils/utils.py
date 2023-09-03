from models.vacancy import Vacancy


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


def sort_vacancies(vacancies: list[Vacancy], reverse=False):
    """Функция для сортировки по зарплате.
    Сортирует по верхней границе. Если ее нет, то
    по нижней.
    """
    return sorted(vacancies, key=sort_by_salary, reverse=reverse)


def filter_vacancies(vacancies: list[Vacancy], words_to_filter: list[str]):
    """Функция фильтрации вакансий по наличию ключевых слов"""
    filtered = []

    for vacancy in vacancies:
        if has_words(vacancy, words_to_filter):
            filtered.append(vacancy)

    return filtered
