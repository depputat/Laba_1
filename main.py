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
class Departmens:
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
    def __init__(self, id: int, med_list: list[str], number: str, data_note: str):
        self.id = id
        self.med_list = med_list
        self.number = number
        self.data_note = data_note


class Diagnosis:
    def __init__(self, id: int, number_mkb: str, description: str):
        self.id = id
        self.number_mkb = number_mkb
        self.description = description


class Record:
    def __init__(
        self, id: int, patient_ids: int, diagnosis_ids: list[int], doctor_id: int
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
        id: int,
        adress: str,
        patient_ids: list[int],
        doctor_id: list[int],
        record_ids: list[int],
        employes_ids: list[int],
        rooms_ids: list[int],
        departmens_ids: list[int],
    ):
        self.id = id
        self.adress = adress
        self.patient_ids = patient_ids
        self.doctor_id = doctor_id
        self.record_ids = record_ids
        self.employes_ids = employes_ids
        self.rooms_ids = rooms_ids
        self.departmens_ids = departmens_ids
