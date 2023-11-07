from FILESaver import FILESaver
import json
import os


class JSONSaver(FILESaver):
    """
    Абстрактный класс для работы с json-файлом вакансий
    """

    file_name = "vacancies.json"

    def add_vacancies(self, vacancies) -> None:
        """
        Добавляет вакансии в json-файл
        """
        if os.stat(self.file_name).st_size == 0:  # если файл пустой
            with open(self.file_name, "w", encoding='utf8') as file:
                json.dump(vacancies, file, indent=2, ensure_ascii=False)  # записываем данные в файл

        else:  # если файл не пустой
            with open(self.file_name, "r", encoding='utf8') as file:
                data = json.load(file)  # выгружаем все данные из файла
                data.extend(vacancies)  # добавляем новые данные
            with open(self.file_name, "w", encoding='utf8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)  # перезаписываем файл

    def filter_vacancies(self, search_word) -> list:
        """
        Возвращает вакансии из json-файла, соответствующие поисковому запросу: search_word
        """

        with open(self.file_name, "r", encoding='utf8') as file:
            data = json.load(file)
            filtered_list = []

            for vacancy in data:
                for key, value in vacancy.items():
                    if search_word.lower() in str(value).lower():
                        filtered_list.append(vacancy)

            return filtered_list

    def top_vacancies(self, top_n) -> list:
        """
        Возвращает top_n вакансий из json-файла, отсортированные по уровню зарплаты
        """

        with open(self.file_name, "r", encoding='utf8') as file:
            data = json.load(file)
            data.sort(key=lambda dictionary: dictionary["salary_from"], reverse=True)

            return data[: top_n]

    def delete_vacancies(self) -> None:
        """
        Удаляет все вакансии из json-файла
        """

        with open(self.file_name, "w", encoding='utf8') as file:
            pass

