class InvalidVacancyObject(Exception):
    def __init__(self, *args, **kwargs):
        self.message = (
            args[0] if args else "Список должен состоять только из объектов Vacancy"
        )
