from typing import List


class Person:
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle_name: str,
        birth_date: str,
        geo: str,
    ):
        self.id = id
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.geo = geo

    @staticmethod
    def from_json(cls, path):
        pass

    @staticmethod
    def from_xml(cls, path):
        pass

    def get_info(self):
        pass


class Employ(Person):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle: str,
        birth_date: str,
        geo: str,
        contract: str,
    ):
        super().__init__(id, name, surname, middle, birth_date, geo)
        self.contract = contract

    @staticmethod
    def from_json(cls, path):
        pass

    @staticmethod
    def from_xml(cls, path):
        pass

    def get_info(self):
        pass


# отделения
class Departments:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Doctor(Employ):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle: str,
        birth_date: str,
        geo: str,
        contract: str,
        specialization: str,
        departament_id: int,
    ):
        super().__init__(id, name, surname, middle, birth_date, geo, contract)
        self.specialization = specialization
        self.departament_id = departament_id


class Inventory:
    def __init__(self, id: int, item: str):
        self.id = id
        self.item = item


class Staff(Employ):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle: str,
        birth_date: str,
        geo: str,
        contract: str,
        dubinka_id: int,
    ):
        super().__init__(id, name, surname, middle, birth_date, geo, contract)
        self.dubinka_id = dubinka_id


class Patient(Person):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle_name: str,
        birth_date: str,
        geo: str,
        number_phone: str,
    ):
        super().__init__(id, name, surname, middle_name, birth_date, geo)
        self.number_phone = number_phone

    @staticmethod
    def from_json(cls, path):
        pass

    @staticmethod
    def from_xml(cls, path):
        pass

    def get_info(self):
        pass


class Recipe:
    def __init__(self, id: int, med_List: List[str], number: str, data_note: str):
        self.id = id
        self.med_List = med_List
        self.number = number
        self.data_note = data_note


class Diagnosis:
    def __init__(self, id: int, number_mkb: str, description: str):
        self.id = id
        self.number_mkb = number_mkb
        self.description = description


class Record:
    def __init__(
        self, id: int, patient_ids: int, diagnosis_ids: List[int], doctor_id: int
    ):
        self.id = id
        self.patient_ids = patient_ids
        self.diagnosis_ids = diagnosis_ids
        self.doctor_id = doctor_id


# кабинеты
class Rooms:
    def __init__(self, id: int, number_room: str, department_id: int):
        self.id = id
        self.number_room = number_room
        self.department_id = department_id


class Clinic:
    def __init__(
        self,
        adress: str,
        patient: List[Patient],
        doctor: List[Doctor],
        record: List[Record],
        employe: List[Employ],
        room: List[Rooms],
        department: List[Departments],
    ):
        self.adress = adress
        self.patient = patient
        self.doctor = doctor
        self.record = record
        self.employe = employe   # cделать самому
        self.room = room   # сделать самому - не можем удалять и добавлять!
        self.department = department  # тоже самое как и room's

    def add_patient(self, patient: Patient):
        self.patient.append(patient)

    def get_patient(self, id: int):
        for item in self.patient:
            if id == item.id:
                return item

    def update_patient(self, id: int, **kwargs):
        patient = self.get_patient(id)

        for key, value in kwargs.items():
            setattr(patient, key, value)

    def delete_patient(self, id: int):
        patient = self.get_patient(id)

        self.patient.remove(patient)

    def get_doctor(self, id: int):
        for item in self.doctor:
            if item.id == id:
                return item

    def add_doctor(self, doctor: Doctor):
        self.doctor.append(doctor)

    def update_doctor(self, id: int, **kwargs):
        doctor = self.get_doctor(id)

        for key, value in kwargs.items():
            setattr(doctor, key, value)

    def delete_doctor(self, id: int):
        doctor = self.get_doctor(id)

        self.doctor.remove(doctor)

    def get_record(self, record: Record):
        for item in self.record:
            if item.id == record:
                return item

    def add_record(self, record: Record):

        self.record.append(record)

    def update_record(self, id: int, **kwargs):

        record = self.get_record(id)

        for key, value in kwargs.items():
            setattr(record, key, value)

    def delete_record(self, id: int):

        record = self.get_record(id)

        self.record.remove(record)


