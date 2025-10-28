from Employe import Employe


class Staff(Employe):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle: str,
        birth_date: str,
        geo: str,
        contract: str,
        dubinka: int,
    ) -> None:
        super().__init__(id, name, surname, middle, birth_date, geo, contract)
        self.dubinka = dubinka

    def get_info(self) -> str:
        return f"Это охранник - {self.surname} {self.name} {self.middle_name}.\nДата рождения: {self.birth_date}.\nМесто проживания: {self.geo}.\nКонтракт: {self.contract}.\nОборонительное оружие: {self.dubinka}"
