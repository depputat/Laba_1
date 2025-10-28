from typing import List


class Record:
    def __init__(
        self,
        id: int,
        patient_id: int,
        diagnosis_ids: List[int],
        doctor_id: int,
        data: str,
        recipe_ids: List[int],
    ) -> None:
        """Инициализация атрибутов записи"""
        self.id = id
        self.patient_id = patient_id
        self.diagnosis_ids = diagnosis_ids
        self.doctor_id = doctor_id
        self.data = data
        self.recipe_ids = recipe_ids

    def get_info(self) -> str:
        """Возвращает информацию о записи"""
        return f"Пациент: {self.patient_id}.\nС диагнозом: {self.diagnosis_ids}.\nРецепты: {self.recipe_ids}.\nПод наблюдением врача: {self.doctor_id}.\nДата приема: {self.data}."
