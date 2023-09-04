import os.path

from savers.csv_saver import CsvSaver

# Создание объекта для тестирования


# Создаем объект сейвера для тестирования
csv_saver = CsvSaver(os.path.join("tests", "testfiles", "test"))
# Очистка загруженных ранее данных
csv_saver.clear()


def test_init():
    assert csv_saver.file_path == "tests/testfiles/test.csv"

    # список вакансий пустой
    assert csv_saver.total_vacancies == 0


def test_add(some_vacancy):
    csv_saver.add_vacancy(some_vacancy)
    assert csv_saver.total_vacancies == 1


def test_delete(some_vacancy, some_vacancy_2, some_vacancy_3):
    csv_saver.delete_vacancy(some_vacancy)
    assert csv_saver.total_vacancies == 0

    csv_saver.add_vacancies([some_vacancy, some_vacancy_2, some_vacancy_3])
    csv_saver.delete_vacancy(some_vacancy_3)

    assert csv_saver.vacancies == [
        some_vacancy,
        some_vacancy_2,
    ]

    csv_saver.delete_vacancy(some_vacancy_2)

    assert csv_saver.vacancies == [
        some_vacancy,
    ]

    csv_saver.delete_vacancy(some_vacancy)


def test_add_vacancies(
    some_vacancy,
    some_vacancy_2,
    some_vacancy_without_salary_to,
    some_vacancy_without_salary_from,
):
    csv_saver.add_vacancies(
        [
            some_vacancy,
            some_vacancy_2,
            some_vacancy_without_salary_to,
            some_vacancy_without_salary_from,
        ]
    )
    assert csv_saver.total_vacancies == 4


def test_get_by_salary():
    vacancies = csv_saver.get_vacancies_by_salary(180000, 190000)
    assert len(vacancies) == 2
