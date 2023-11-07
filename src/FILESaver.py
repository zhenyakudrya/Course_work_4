from abc import ABC, abstractmethod


class FILESaver(ABC):
    """Абстрактный класс для работы с файлом вакансий """

    @abstractmethod
    def add_vacancies(self, vacancies) -> None:
        """
        Добавляет вакансии в файл
        """
        pass

    @abstractmethod
    def filter_vacancies(self, search_word) -> list:
        """
        Возвращает вакансии из json-файла, соответствующие поисковому запросу: search_word
        """
        pass

    @abstractmethod
    def top_vacancies(self, top_n) -> list:
        """
        Возвращает top_n вакансий из json-файла, отсортированные по уровню зарплаты
        """

    @abstractmethod
    def delete_vacancies(self) -> None:
        """
        Удаляет все вакансии из файла
        """
        pass
