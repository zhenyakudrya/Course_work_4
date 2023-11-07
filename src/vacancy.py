class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, title, url, salary, employer) -> None:
        """ Создание экземпляра класса Vacancy
            - title: название вакансии
            - url: ссылка на вакансию
            - salary: зарплата(от)
            - employer: работодатель
        """
        self.title = title
        self.url = url
        self.salary = salary
        self.employer = employer

    def __repr__(self) -> str:
        """
        Возвращает информацию об объекте: название класса(атрибуты экземпляра)
        """
        return f'{self.__class__.__name__}({self.title}, {self.url}, {self.salary}, {self.employer}'

    def __str__(self) -> str:
        """
        Возвращает информацию о вакансии: название(ссылка)
        """
        return f"{self.title} ({self.url})"

    @staticmethod
    def _is_valid_title(title) -> bool:
        """
        Проверка названия вакансии
        """
        return len(title) > 0 and isinstance(title, str)

    @staticmethod
    def _is_valid_url(url) -> bool:
        """
        Проверка названия ссылки на вакансию
        """
        return url.startswith('http://') and isinstance(url, str)

    @staticmethod
    def _is_valid_salary(salary) -> bool:
        """
        Проверка названия зарплаты
        """
        return isinstance(salary, int)

    @staticmethod
    def _is_valid_employer(employer) -> bool:
        """
        Проверка названия работодателя
        """
        return len(employer) > 0 and isinstance(employer, str)

    def __setattr__(self, key, value):
        """
        Валидирует данные, которыми инициализируются атрибуты экземпляра
        """
        if key == 'title' and not self._is_valid_title(value):
            raise Exception("Название вакансии не может быть пустым и должно быть строкой")
        if key == 'salary' and not self._is_valid_salary(value):
            raise Exception("Зарплата должна быть числом")
        if key == 'employer' and not self._is_valid_employer(value):
            raise Exception("Название работодателя не может быть пустым и должно быть строкой")
        super().__setattr__(key, value)

    def __gt__(self, other) -> bool:
        """
        Возвращает результат сравнения(>) зарплаты двух вакансий
        """
        return self.salary > other.salary

    def __it__(self, other) -> bool:
        """
        Возвращает результат сравнения(<) зарплаты двух вакансий
        """
        return self.salary < other.salary
