from abc import ABC, abstractmethod

from models.vacancy import Vacancy


class Saver(ABC):
    """Абстрактный класс для класса сохранения данных в файл"""

    def __init__(self):
        self.vacancies = []

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load_data(self) -> None:
        pass

    def add_vacancy(self, vacancy: Vacancy, save_data=True):
        """Добавить объект вакансии в файл"""
        self.vacancies.append(vacancy)
        if save_data:
            self.save()

    def add_vacancies(self, vacancies: list[Vacancy], save_data=True):
        """Добавить список объектов вакансий в файл"""
        for vacancy in vacancies:
            self.add_vacancy(vacancy, save_data=False)
        self.save()

    def delete_vacancy(self, vacancy: Vacancy):
        """Удалить вакансию из файла"""
        self.vacancies.remove(vacancy)
        self.save()

    def get_vacancies_by_salary(self, salary_from=0, salary_to=float("inf")):
        filtered_vacancies = []
        for vacancy in self.vacancies:
            # Если у вакансии не указана зарплата, пропускаем ее
            if not vacancy.salary_from and not vacancy.salary_to:
                continue
            # Если указан только верхний предел зарплаты
            if not vacancy.salary_from and vacancy.salary_to:
                if vacancy.salary_to >= salary_from:
                    filtered_vacancies.append(vacancy)
            # Если указан только нижний предел зарплаты
            elif not vacancy.salary_to and vacancy.salary_from:
                if salary_from <= vacancy.salary_from <= salary_to:
                    filtered_vacancies.append(vacancy)
            # Если указаны оба предела зарплаты
            else:
                if (
                    salary_from <= vacancy.salary_to
                    and salary_to >= vacancy.salary_from
                ):
                    filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def get_all_vacancies(self):
        return self.vacancies

    def clear(self):
        self.vacancies.clear()
        self.save()
