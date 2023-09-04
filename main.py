import os

import enquiries
import tqdm

import config
from utils import actions
from utils.table import table


def main():
    # Список для дальнейшего хранения вакансий
    all_vacancies = []

    input(
        "Вас приветствует приложение для удобного сбора вакансий с разных платформ!\n"
        "Нажмите enter, чтобы продолжить\n"
    )

    # Проверка, на присутствие в переменных среды API-ключа для SuperJob.
    # При отсутствии ключа, SuperJob не будет предложен в качестве платформы.
    sj_api_key = os.getenv("SJ_API_KEY")

    if not sj_api_key:
        user_input = input(
            '\nВ Вашем окружении отсутствует переменная "SJ_API_KEY" с API-ключом для SuperJob.\n'
            "Для использования API SuperJob, закройте это приложение (CTRL + C), и добавьте Ваш API-ключ командой \n"
            "export SJ_API_KEY={ваш API-ключ}\n"
            "Без ключа поиск на этой платформе не будет произведен.\n"
            "Нажмите enter, чтобы продолжить..."
        )

        del config.PARSERS["SuperJob"]

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

    # Добавить и сохранить все вакансии в файле
    saver.add_vacancies(all_vacancies)

    # Запрос на фильтрацию по зарплате
    if enquiries.confirm("Отфильтровать вакансии по зарплате?"):
        vacancies = actions.filter_by_salary(saver)
    else:
        vacancies = all_vacancies

    # Запрос на фильтрацию по ключевым словам
    if enquiries.confirm("Отфильтровать вакансии по ключевым словам?"):
        filter_words = input("Введите слова для поиска через пробел -> ").split()
        vacancies = actions.filter_by_keywords(vacancies, filter_words)

    # Запрос на сортировку
    if enquiries.confirm("Отсортировать вакансии по зарплате?"):
        vacancies = actions.sort_vacancies(vacancies)

    # Вывод данных
    if not vacancies:
        print("Не нашлось вакансий с выбранными критериями")
    else:
        # Добавляем данные в таблицу
        table.add_vacancies(vacancies)

        # Печать таблицы
        print(table)

        # Цикл работы с вакансиями индивидуально
        while True:
            user_vacancy_choice = input(
                "\nВведите номер вакансии для выбора действия -> "
            )

            if not user_vacancy_choice.isdigit() or not 1 <= int(
                user_vacancy_choice
            ) <= len(vacancies):
                print(f"\nНомер должен быть целым числом от 1 до {len(vacancies)}")
                continue

            chosen_vacancy = vacancies[int(user_vacancy_choice) - 1]

            # Варианты пользовательских действий
            vacancy_actions = {
                "Посмотреть полную информацию": "review",
                "Удалить вакансию": "delete",
                "Выбрать другую вакансию": "continue",
                "Закончить работу": "exit",
            }

            user_action = enquiries.choose(
                "\nВыберете дальнейшее действие с вакансией",
                vacancy_actions,
                multi=False,
            )

            if user_action == "review":
                print(chosen_vacancy)
            elif user_action == "delete":
                saver.delete_vacancy(chosen_vacancy)
                vacancies.remove(chosen_vacancy)

                # Обновление таблицы и вывод
                table.clear()
                table.add_vacancies(vacancies)
                print(table)
            elif user_action == "continue":
                continue
            elif user_action == "exit":
                break

    print("\nПриложение завершает работу. Хорошего дня!")


if __name__ == "__main__":
    main()
