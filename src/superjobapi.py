from JobSiteAPI import JobSiteAPI
import os
import requests
import json
from exceptions import ParsingError


class SuperJobAPI(JobSiteAPI):
    __API_KEY: str = os.getenv('SJ_API_KEY')
    __url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, keyword) -> list:
        req = requests.get(self.__url,
                           headers={"X-Api-App-Id": self.__API_KEY},
                           params={'keywords': keyword, 'page': 0, 'count': 100})
        if req.status_code != 200:
            raise ParsingError('Ошибка получения вакансий!')
        req_json = req.json()
        vacancies_list = []
        for r in req_json["objects"]:
            vacancies_dict = {"vacancy_name": r['profession'],
                              "vacancy_url": r["link"],
                              "vacancy_salary": f'От {r["payment_from"]} до {r["payment_to"]} {r["currency"]}',  # Исправить!!!
                              "vacancy_description": r["candidat"]}
            vacancies_list.append(vacancies_dict)
            print(vacancies_dict['vacancy_salary'])
        return vacancies_list

# sj = SuperJobAPI()
# data = sj.get_vacancies('Python')
# with open("sj.json", "w", encoding='utf-8') as json_file:
#     json.dump(data, json_file, indent=4, sort_keys=True)
# # for item in data['objects']:
# #     print(item)