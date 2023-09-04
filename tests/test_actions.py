from utils import actions


def test_filter_by_keywords(
    vacancy_python_php, vacancy_python_java_go, vacancy_python_java
):

    # Проверка фильтрации по одному слову
    vacancies = [vacancy_python_php, vacancy_python_java_go]
    search_query = "php"
    search_query = search_query.split()

    filtered = actions.filter_by_keywords(vacancies, search_query)

    assert filtered == [vacancy_python_php]

    # проверка фильтрации по нескольким словам

    search_query = "java go".split()
    filtered = actions.filter_by_keywords(vacancies, search_query)

    assert filtered == [vacancy_python_java_go]
