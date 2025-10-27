# кабинеты
class Rooms:
    def __init__(self, id: int, number_room: str, department_id: int) -> None:
        self.id = id
        self.number_room = number_room
        self.department_id = department_id

    def get_info(self) -> str:
        return f"Комната №{self.number_room}.\nПринадлежит отделению: {self.department_id}."
