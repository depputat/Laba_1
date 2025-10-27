class Person:
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle_name: str,
        birth_date: str,
        geo: str,
    ) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.geo = geo

    def get_info(self) -> str:
        return f"Это человек, которого зовут: {self.surname} {self.name} {self.middle_name}.\nДата рождения: {self.birth_date}.\nМесто проживания: {self.geo}."
