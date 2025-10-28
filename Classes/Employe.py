from Classes.Person import Person


class Employe(Person):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle_name: str,
        birth_date: str,
        geo: str,
        contract: str,
    ) -> None:
        """Инициализация атрибутов сотрудника"""
        super().__init__(id, name, surname, middle_name, birth_date, geo)
        self.contract = contract

    def get_info(self) -> str:
        """Возвращает информацию о сотруднике"""
        return f"Работник поликлиники - {self.surname} {self.name} {self.middle_name}.\nКонтракт: {self.contract}.\nМесто проживания: {self.geo}."
