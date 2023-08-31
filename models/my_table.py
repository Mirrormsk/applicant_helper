from prettytable import PrettyTable

from models.vacancy import Vacancy


class MyTable(PrettyTable):
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        """Принимает список вакансий и добавляет их в таблицу"""

        self.add_rows(
            [
                [num] + vacancy.to_print()
                for num, vacancy in enumerate(vacancies, start=1)
            ]
        )

