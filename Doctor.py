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
        departament_id: int,
    ) -> None:
        super().__init__(id, name, surname, middle_name, birth_date, geo, contract)
        self.specialization = specialization
        self.departament_id = departament_id

    def get_info(self) -> str:
        return f"Это врач: {self.surname} {self.name} {self.middle_name}.\nСпециализация: {self.specialization}.\nРаботает в {self.departament_id} отделении."
