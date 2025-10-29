class Diagnosis:
    """Класс, представляющий диагнозы пациентов.
    Содержит номер и расшифровку диагноза"""

    def __init__(self, id: int, number_mkb: str, description: str) -> None:
        """Инициализация атрибутов диагнозов"""
        self.id = id
        self.number_mkb = number_mkb
        self.description = description

    def get_info(self) -> str:
        """Возвращает информацию о диагнозе"""
        return f"Диагноз №{self.number_mkb}.\nРасшифровка: {self.description}."
