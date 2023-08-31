class InvalidJSONData(Exception):
    """Класс исключения для неверных данных о вакансии на входе"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неверные JSON данные"


class InvalidCSVRow(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неверные данные в строке CSV-файла"
