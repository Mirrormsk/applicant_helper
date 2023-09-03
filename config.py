from parsers import HeadHunterParser, SuperJobParser
from savers import JSONSaver, CsvSaver


# Имя директории для хранения результатов
DATA_DIR = "data"

# Словарь с парсерами для разных платформ
PARSERS = {
    "HeadHunter": HeadHunterParser,
    "SuperJob": SuperJobParser,
}

# Словарь с классами для сохранения в файл
SAVERS = {
    "json": JSONSaver,
    "csv": CsvSaver,
}


# Конфигурация таблицы вывода
class Table:

    # Заголовки таблицы
    th = [
        # "ID",
        "№",
        "Название",
        "З/п от",
        "З/п до",
        "Валюта",
        "Расположение",
        # "Адрес",
        "Ссылка",
        "Требования",
        # "Обязанности",
        "Работодатель",
    ]

    # Максимальная ширина таблицы в символах
    max_table_width = 130

    # Минимальная ширина ячейки
    min_width = 120
