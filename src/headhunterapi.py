from JobSiteAPI import JobSiteAPI
import requests


class HeadHunterAPI(JobSiteAPI):
    """
    Класс для работы с API сайта с вакансиями: hh.ru
    """

    def __init__(self):
        """
        Создание экземпляра класса HeadHunterAPI
        """
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword) -> dict:
        """
        Возвращает отфильтрованные по ключевому слову вакансии с сайта
        """
        params = {
            "text": keyword,  # ключевое слово фильтра
            "area": 1,  # город поиска работы(1 - Москва)
            "per_page": 50,  # количество вакансий
        }
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Запрос не выполнен, код ошибки: {response.status_code}")

    @staticmethod
    def standard_vacancies(data) -> list:
        """
        Приводит данные к единому стандарту
        """
        standard_vacancies = []
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            try:
                vacancy_salary_from = vacancy.get("salary", {}).get("from")
                if vacancy_salary_from is None:
                    vacancy_salary_from = 0
            except AttributeError:
                vacancy_salary_from = 0
            vacancy_employer = vacancy.get("employer", {}).get("name")

            standard_vacancies.append({"title": vacancy_title,
                                       "url": vacancy_url,
                                       "salary_from": vacancy_salary_from,
                                       "employer": vacancy_employer})

        return standard_vacancies
