class Diagnosis:
    def __init__(self, id: int, number_mkb: str, description: str) -> None:
        self.id = id
        self.number_mkb = number_mkb
        self.description = description

    def get_info(self) -> str:
        return f"Диагноз №{self.number_mkb}.\nРасшифровка: {self.description}."