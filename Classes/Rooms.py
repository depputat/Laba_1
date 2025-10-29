class Rooms:
    """Класс, представляющий кабинеты поликлиники.
    Содержит информацию о номере кабинета и привязке отделения"""

    def __init__(self, id: int, number_room: str, department_id: int) -> None:
        """Инициализация медицинских кабинетов в поликлинике"""
        self.id = id
        self.number_room = number_room
        self.department_id = department_id

    def get_info(self) -> str:
        """Возвращает информацию о медицинских кабинетах в поликлинике"""
        return f"Комната №{self.number_room}.\nПринадлежит отделению: {self.department_id}."
