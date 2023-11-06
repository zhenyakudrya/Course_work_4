from JobSiteAPI import JobSiteAPI
import requests
import json
from exceptions import ParsingError


class HeadHunterAPI(JobSiteAPI):
    __url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, keyword) -> list:
        req = requests.get(self.__url,
                           params={'text': f'NAME:{keyword}', 'page': 0, 'per_page': 100})
        if req.status_code != 200:
            raise ParsingError('Ошибка получения вакансий!')
        req_json = req.json()
        vacancies_list = []
        for r in req_json["items"]:
            vacancies_dict = {"vacancy_name": r["name"],
                              "vacancy_url": r["alternate_url"],
                              "vacancy_salary": f'{r["salary"]["from"]}-{r["salary"]["to"]}', #Проверить
                              "vacancy_description": r["snippet"]["responsibility"]}
            vacancies_list.append(vacancies_dict)
        return vacancies_list


# hh = HeadHunterAPI()
# data = hh.get_vacancies('Python')
# with open("vacancies.json", "w", encoding='utf-8') as json_file:
#     json.dump(data, json_file, indent=4, sort_keys=True)
# for item in data['items']:
#     print(item['salary'])

