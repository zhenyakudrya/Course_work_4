from headhunterapi import HeadHunterAPI
from superjobapi import SuperJobAPI
from vacancy import Vacancy


def user_interaction():
    """ Обработка запроса пользователя и вывод информации """
    ''' Сценарии использования
        1. Поиск вакансий
            1. Поиск вакансии
                Запросить платформу HH SJ или оба
                Запросить ключевое слово (слова если расширенный поиск и где искать: везде, только название, название фирмы)        
        2. Работа с найденными вакансиями
            1. Сортировка найденных вакансий
                Указать параметр сортировки (зарплата, название, фирма)
                Указать количество вакансий  
            2. Сохранение данных в файл (JSON)
                Выбрать формат и имя файла
                Выбрать параметры выбора вакансий
            3. Вывод на экран'''

    question = input('Выберете платформу для поиска вакансий: 1 - HeadHunter\n'
                     '                                        2 - SuperJob\n'
                     '                                        3 - Обе платформы\n'
                     ' ')
    if question == 1:
        keyword = input('Введите ключевое слово для поиска: ')
        hh = HeadHunterAPI()
        vacancies_list = hh.get_vacancies(f'{keyword}')
        sort_param = input('Введите параметр для сортировки: 1 - Название вакансии, 2 - Зарплата ')
        if sort_param == 1:
            pass
        elif sort_param == 2:
            pass
    elif question == 2:
        keyword = input('Введите ключевое слово для поиска: ')
        sj = SuperJobAPI()
        vacancies_list = sj.get_vacancies(f'{keyword}')
        sort_param = input('Введите параметр для сортировки: 1 - Название вакансии, 2 - Зарплата ')
        if sort_param == 1:
            pass
        elif sort_param == 2:
            pass
    elif question == 3:
        keyword = input('Введите ключевое слово для поиска: ')
        hh = HeadHunterAPI()
        sj = SuperJobAPI()
        vacancies_list = hh.get_vacancies(f'{keyword}') + sj.get_vacancies(f'{keyword}')
        sort_param = input('Введите параметр для сортировки: 1 - Название вакансии, 2 - Зарплата ')
        if sort_param == 1:
            pass
        elif sort_param == 2:
            pass
    else:
        print('Вы не выбрали платформу для поиска')

# kkk = user_interaction()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)