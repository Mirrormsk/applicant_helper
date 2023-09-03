import os
import csv
from models.vacancy import Vacancy
from savers.saver import Saver


class CsvSaver(Saver):
    def __init__(self, file_name: str):

        self.file_path = file_name + ".csv"
        super().__init__()
        self.load_data()

        self.headers = [
            "id",
            "name",
            "salary_from",
            "salary_to",
            "area",
            "full_address",
            "url",
            "requirements",
            "employer",
        ]

    def save(self):

        data = [vacancy.to_list() for vacancy in self.vacancies]
        with open(self.file_path, "w", encoding="utf-8", newline="") as file_out:
            writer = csv.writer(file_out, delimiter=";")
            writer.writerow(self.headers)
            writer.writerows(data)

    def load_data(self) -> None:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file_in:
                reader = csv.reader(file_in, delimiter=";")

                # пропускаем строку заголовков
                next(reader)

                # формируем список объектов
                self.vacancies = [Vacancy.from_list(line) for line in reader]
