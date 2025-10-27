from Person import Person
class Patient(Person):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle_name: str,
        birth_date: str,
        geo: str,
        number_phone: str,
    ) -> None:
        super().__init__(id, name, surname, middle_name, birth_date, geo)
        self.number_phone = number_phone

    def get_info(self) -> str:
        return f"Пациент - {self.surname} {self.name} {self.middle_name}.\nДата рождения: {self.birth_date}.\nМесто проживания: {self.geo}.\nНомер телефона: {self.number_phone}."
