class Departments:
    """Отделения поликлиники"""

    def __init__(self, id: int, name: str) -> None:
        """Инициализация атрибутов отделения поликлиники"""
        self.id = id
        self.name = name

    def get_info(self) -> str:
        """Возвращает информацию об отделении"""
        return f"Это отделение - {self.name}."
