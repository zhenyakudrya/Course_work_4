from JobSiteAPI import JobSiteAPI
import os
import requests


class HeadHunterAPI(JobSiteAPI):
    __url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, keyword) -> dict:
        req = requests.get(self.__url,
                           params={'text': f'NAME:{keyword}', 'page': 0, 'per_page': 100}).json()
        return req



