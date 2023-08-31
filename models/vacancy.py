from exceptions.vacancy_exceptions import *


class Vacancy:
    def __init__(
        self,
        id: int,
        name: str,
        salary_from: int,
        salary_to: int,
        currency: str,
        area: str,
        full_address: str,
        url: str,
        requirements: str,
        employer: str,
    ):
        self.id = id
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.area = area
        self.full_address = full_address
        self.url = url
        self.employer = employer

        if requirements:
            requirements = requirements.replace("<highlighttext>", "").replace(
                "</highlighttext>", ""
            )

        self.requirements = requirements

        if currency.lower() in ("rur", "rub"):
            self.currency = "RUB"
        else:
            self.currency = currency.upper()

    def to_list(self):
        # th = ['ID', 'Название', 'Расположение', 'З/п от', 'З/п до']
        return [
            self.id,
            self.name,
            self.salary_from,
            self.salary_to,
            self.currency,
            self.area,
            self.full_address,
            self.url,
            self.requirements,
            self.employer,
        ]

    @classmethod
    def from_list(cls, array: list):
        """
        Метод для создания экземпляра из списка
        :param array: список с данными формата
        ["id", "name", "salary_from", "salary_to",
        "currency", "area", "full_address", "url",
        "requirement", "employer"]

        :return: объект Vacancy
        """

        # Валидация данных
        if len(array) != 10:
            raise InvalidCSVRow

        return cls(*array)

    def to_dict(self):
        """Возвращает данные вакансии в виде списка"""
        return {
            "id": self.id,
            "name": self.name,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency,
            "area": self.area,
            "full_address": self.full_address,
            "url": self.url,
            "requirement": self.requirements,
            "employer": self.employer,
        }

    @classmethod
    def from_dict(cls, vacancy_dict: dict):
        """
        Метод для создания экземпляра из словаря
        :param vacancy_dict: словарь с данными
        :return: объект Vacancy
        """

        # Валидация данных
        if list(vacancy_dict.keys()) != [
            "id",
            "name",
            "salary_from",
            "salary_to",
            "currency",
            "area",
            "full_address",
            "url",
            "requirement",
            "employer",
        ]:
            raise InvalidJSONData

        return cls(
            id=vacancy_dict["id"],
            name=vacancy_dict["name"],
            salary_from=vacancy_dict["salary_from"],
            salary_to=vacancy_dict["salary_to"],
            currency=vacancy_dict["currency"],
            area=vacancy_dict["area"],
            full_address=vacancy_dict["full_address"],
            url=vacancy_dict["url"],
            requirements=vacancy_dict["requirement"],
            employer=vacancy_dict["employer"],
        )

    @property
    def short_requirements(self):
        """Свойство для короткого отображения требований по вакансии"""
        return self.requirements[:100] + "..." if self.requirements else ""

    def to_print(self):
        """
        Метод для вывода данных в таблицу
        :return: список с нужными строковыми данными
        """

        return [
            # self.id,
            self.name,
            self.salary_from if self.salary_from else 0,
            self.salary_to if self.salary_to else 0,
            self.currency,
            self.area,
            self.url,
            self.short_requirements,
            self.employer,
        ]

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, name='{self.name}', "
            f"salary_from={self.salary_from}, salary_to={self.salary_to}, "
            f"currency='{self.currency}', area='{self.area}', "
            f"full_address='{self.full_address}', url='{self.url}', "
            f"requirements='{self.requirements}', employer='{self.employer}')"
        )

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError(
                f"Класс  {self.__class__} поддерживает сравнение только"
                f"с экземплярами своего класса"
            )
        return max(self.salary_from, self.salary_to) == max(
            other.salary_from, other.salary_to
        )

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError(
                f"Класс  {self.__class__} поддерживает сравнение только"
                f"с экземплярами своего класса"
            )
        return max(self.salary_from, self.salary_to) < max(
            other.salary_from, other.salary_to
        )

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError(
                f"Класс  {self.__class__} поддерживает сравнение только"
                f"с экземплярами своего класса"
            )
        return max(self.salary_from, self.salary_to) <= max(
            other.salary_from, other.salary_to
        )

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError(
                f"Класс  {self.__class__} поддерживает сравнение только"
                f"с экземплярами своего класса"
            )
        return max(self.salary_from, self.salary_to) > max(
            other.salary_from, other.salary_to
        )

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError(
                f"Класс  {self.__class__} поддерживает сравнение только"
                f"с экземплярами своего класса"
            )
        return max(self.salary_from, self.salary_to) >= max(
            other.salary_from, other.salary_to
        )
