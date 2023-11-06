from FILESaver import FILESaver
import json


class JSONSaver(FILESaver):
    def add_vacancy(self, vacancy_list):
        with open("vacancies.json", "w", encoding='utf-8') as json_file:
            json.dump(vacancy_list, json_file, indent=4, sort_keys=True)

    def get_vacancies_by_salary(self):
        # desc = True if input(
        #     'От - \n'
        #     'До - '
        # ).lower() == '>' else False
        # vacancies = ...
        # return sorted(vacancies, key=lambda x: (x.salary_from if x.salary_from else 0, x.salary_to if x.salary_to else 0), reverse=desc)

    def delete_vacancy(self):
        with open("vacancies.json", "w") as f:
            pass

