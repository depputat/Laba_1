# отделения
class Departments:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def get_info(self) -> str:
        return f"Это отделение - {self.name}."
