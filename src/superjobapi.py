from JobSiteAPI import JobSiteAPI
import os
import requests


class SuperJobAPI(JobSiteAPI):
    __API_KEY: str = os.getenv('SJ_API_KEY')
    __url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, keyword) -> dict:
        req = requests.get(self.__url,
                           headers={"X-Api-App-Id": self.__API_KEY},
                           params={'keywords': keyword, 'page': 0, 'count': 100}).json()
        return req



