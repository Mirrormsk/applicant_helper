import os.path

from savers.json_saver import JSONSaver

# Создаем объект сейвера для тестирования
json_saver = JSONSaver(os.path.join("tests", "testfiles", "test"))
# Очистка загруженных ранее данных
json_saver.clear()


def test_init():
    assert json_saver.file_path == "tests/testfiles/test.json"

    # список вакансий пустой
    assert json_saver.total_vacancies == 0


def test_add(some_vacancy):
    json_saver.add_vacancy(some_vacancy)
    assert json_saver.total_vacancies == 1


def test_delete(some_vacancy):
    json_saver.delete_vacancy(some_vacancy)
    assert json_saver.total_vacancies == 0


def test_add_vacancies(
    some_vacancy,
    some_vacancy_2,
    some_vacancy_without_salary_to,
    some_vacancy_without_salary_from,
):
    json_saver.add_vacancies(
        [
            some_vacancy,
            some_vacancy_2,
            some_vacancy_without_salary_to,
            some_vacancy_without_salary_from,
        ]
    )
    assert json_saver.total_vacancies == 4

    json_saver.clear()
