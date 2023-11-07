from vacancy import Vacancy


def user_print(vacancies: list) -> list[Vacancy]:
    """
    Из листа вакансий формирует наглядный для пользователя перечень экземпляров класса Vacancy
    """

    vacancy_class_list = []
    for vacancy in vacancies:
        vacancy_class_list.append(
            Vacancy(vacancy["title"], vacancy["url"], vacancy["salary_from"], vacancy["employer"]))

    return vacancy_class_list
