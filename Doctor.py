from Employe import Employe
class Doctor(Employe):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle_name: str,
        birth_date: str,
        geo: str,
        contract: str,
        specialization: str,
        department_id: int,
    ) -> None:
        super().__init__(id, name, surname, middle_name, birth_date, geo, contract)
        self.specialization = specialization
        self.department_id = department_id

    def get_info(self) -> str:
        return f"Это врач: {self.surname} {self.name} {self.middle_name}.\nСпециализация: {self.specialization}.\nРаботает в {self.department_id} отделении."
