import os

import enquiries
import tqdm

import config
from utils.table import table


def main():
    # Список для дальнейшего хранения вакансий
    all_vacancies = []

    # Начальный выбор платформ для сбора вакансий
    while True:

        chosen_platforms = enquiries.choose(
            "Выберете платформы для поиска вакансий (нажмите пробел для подтверждения): ",
            config.PARSERS,
            multi=True,
        )

        if chosen_platforms:
            break
        else:
            print(f"Выберите хотя бы одну платформу. Нажмите пробел для выбора.")

    # Получение запроса пользователя
    while True:
        user_query = input("Введите запрос для поиска -> ")
        if not user_query:
            print("Введен пустой запрос. Повторите ввод.")
        else:
            break

    # Сбор вакансий
    for platform in tqdm.tqdm(chosen_platforms, desc="Сбор данных с платформ"):
        platform = platform()
        platform_vacancies = platform.get_vacancies(user_query)
        all_vacancies.extend(platform_vacancies)

    print(f"Всего найдено {len(all_vacancies)} вакансий.")

    # Выбор формата для сохранения результатов в файл
    saver_choice = enquiries.choose(
        "Выберете формат для сохранения вакансий:",
        config.SAVERS,
        multi=False,
    )

    filename = input("Введите имя файла для сохранения (без расширения) -> ")

    # Создание объекта для сохранения результатов в файл
    saver = saver_choice(os.path.join(config.DATA_DIR, filename))

    # Если файл не пустой, спрашиваем пользователя удалять ли старые вакансии
    if saver.vacancies:

        if enquiries.confirm(
            f"Файл с таким именем уже существует, и содержит {len(saver.vacancies)} записей. \
            Удалить сохраненные записи?"
        ):
            saver.clear()
            print("Старые данные удалены.\n")

    saver.add_vacancies(all_vacancies)

    vacancies = saver.get_vacancies_by_salary(100_000, 150_000)

    # Добавляем данные в таблицу

    table.add_vacancies(vacancies)

    # print(table)

    chosen_vacancy = vacancies[
        int(input("Ввыдите номер вакансии для выбора действия -> ")) - 1
    ]

    print(chosen_vacancy)


if __name__ == "__main__":
    main()
