from abc import ABC, abstractmethod


class FILESaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass

