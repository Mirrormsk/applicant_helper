import json
import os

from models.vacancy import Vacancy
from savers.saver import Saver


class JSONSaver(Saver):
    def __init__(self, file_name: str):
        self.file_path = file_name + ".json"
        super().__init__()
        self.load_data()

    def load_data(self) -> None:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file_in:
                data = json.load(file_in)
                vacancies = [Vacancy.from_dict(vacancy_dict) for vacancy_dict in data]
                self.vacancies = vacancies

    def save(self):
        data = [vacancy.to_dict() for vacancy in self.vacancies]
        with open(self.file_path, "w", encoding="utf-8") as file_out:
            json.dump(data, file_out, indent=4, ensure_ascii=False)
