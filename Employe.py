from Person import Person
class Employe(Person):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle: str,
        birth_date: str,
        geo: str,
        contract: str,
    ) -> None:
        super().__init__(id, name, surname, middle, birth_date, geo)
        self.contract = contract

    def get_info(self) -> str:
        return f"Работник поликлиники - {self.surname} {self.name} {self.middle_name}.\nКонтракт: {self.contract}.\nМесто проживания: {self.geo}."
