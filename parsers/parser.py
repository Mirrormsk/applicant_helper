from abc import ABC, abstractmethod

from models.vacancy import Vacancy


class APIParser(ABC):
    @abstractmethod
    def get_vacancies(self, query) -> list[Vacancy]:
        pass
