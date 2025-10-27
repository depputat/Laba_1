from typing import List

class Recipe:
    def __init__(
        self, id: int, med_list: List[str], number: str, data_note: str
    ) -> None:
        self.id = id
        self.med_list = med_list
        self.number = number
        self.data_note = data_note

    def get_info(self) -> str:
        return f"Это рецепт.\nНомер рецепта: {self.number}.\nДата записи: {self.data_note}.\nСодержимое рецепта: {self.med_list}."
