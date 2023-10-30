class Vacancy:
    """
    Класс должен поддерживать методы сравнения вакансий между собой по зарплате
    и валидировать данные, которыми инициализируются его атрибуты.
    """

    def __init__(self, vacancy_name, vacancy_url, vacancy_salary, vacancy_description):
        self.vacancy_name = vacancy_name
        self.vacancy_url = vacancy_url
        self.vacancy_salary = vacancy_salary
        self.vacancy_description = vacancy_description

    def __gt__(self, other):
        return int(self.vacancy_salary) > int(other.vacancy_salary)

    def __lt__(self, other):
        return int(self.vacancy_salary) < int(other.vacancy_salary)

    def __eq__(self, other):
        return int(self.vacancy_salary) == int(other.vacancy_salary)
