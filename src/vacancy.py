import json


class Vacancy:
    """
    Класс должен поддерживать методы сравнения вакансий между собой по зарплате
    и валидировать данные, которыми инициализируются его атрибуты.
    """
    vacancies = []

    def __init__(self, vacancy_name, vacancy_url, vacancy_salary, vacancy_description):
        self.vacancy_name = vacancy_name
        self.vacancy_url = vacancy_url
        self.vacancy_salary = vacancy_salary
        self.vacancy_description = vacancy_description

    def __repr__(self):
        return f'Vacancy({self.vacancy_name}, {self.vacancy_url}, {self.vacancy_salary}, {self.vacancy_description})'

    def __gt__(self, other):
        return int(self.vacancy_salary) > int(other.vacancy_salary)

    def __lt__(self, other):
        return int(self.vacancy_salary) < int(other.vacancy_salary)

    def __eq__(self, other):
        return int(self.vacancy_salary) == int(other.vacancy_salary)

    @classmethod
    def from_list(cls, vacancies_list):
        for item in vacancies_list:
            vac = Vacancy(f"{item['vacancy_name']}", f"{item['vacancy_url']}", f"{item['vacancy_salary']}",
                          f"{item['vacancy_description']}")
            cls.vacancies.append(vac)

    @classmethod
    def sort_by_salary(cls):
        cls.vacancies.sort(key=lambda x: x.vacancy_salary, reverse=True)

    @classmethod
    def sort_by_name(cls):
        cls.vacancies.sort(key=lambda x: x.vacancy_name, reverse=True)


# file = 'vacancies.json'
#
# with open(file, "r") as my_file:
#     vacancies_json = my_file.read()
#
# vacancies = json.loads(vacancies_json)
#
# Vacancy.from_list(vacancies)
# Vacancy.sort_by_salary()

