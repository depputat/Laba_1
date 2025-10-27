from typing import List
class Record:
    def __init__(
        self,
        id: int,
        patient_id: int,
        diagnosis_ids: List[int],
        doctor_id: int,
        data: str,
    ) -> None:
        self.id = id
        self.patient_id = patient_id
        self.diagnosis_ids = diagnosis_ids
        self.doctor_id = doctor_id
        self.data = data

    def get_info(self) -> str:
        return f"Пациент: {self.patient_id}.\nС диагнозом: {self.diagnosis_ids}.\nПод наблюдением врача: {self.doctor_id}.\nДата приема: {self.data}."
