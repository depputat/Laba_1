from typing import List


class Recipe:
    """Класс, представляющий медицинский рецепт.
    Содержит информацию о списке 'препаратов', номере рецепта и дате рецепта"""

    def __init__(
        self, id: int, med_list: List[str], number: str, data_note: str
    ) -> None:
        """Инициализация атрибутов медицинского рецепта"""
        self.id = id
        self.med_list = med_list
        self.number = number
        self.data_note = data_note

    def get_info(self) -> str:
        """Возвращает информацию о медицинском рецепте"""
        return f"Это рецепт.\nНомер рецепта: {self.number}.\nДата записи: {self.data_note}.\nСодержимое рецепта: {self.med_list}."
