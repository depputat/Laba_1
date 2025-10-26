from typing import List
import json
import xml.etree.ElementTree as ET

class Person:
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle_name: str,
        birth_date: str,
        geo: str,
    ) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.geo = geo

    def get_info(self) -> str:
        return f"Это человек, которого зовут: {self.surname} {self.name} {self.middle_name}.\nДата рождения: {self.birth_date}.\nМесто проживания: {self.geo}."


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
    ) -> None:
        super().__init__(id, name, surname, middle, birth_date, geo)
        self.contract = contract

    @staticmethod
    def from_json(cls, path) -> None:
        pass

    @staticmethod
    def from_xml(cls, path) -> None:
        pass

    def get_info(self) -> str:
        return f"Работник поликлиники - {self.surname} {self.name} {self.middle_name}.\nКонтракт: {self.contract}.\nМесто проживания: {self.geo}."


# отделения
class Departments:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def get_info(self) -> str:
        return f"Это отделение - {self.name}."


class Doctor(Employ):
    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        middle_name: str,
        birth_date: str,
        geo: str,
        contract: str,
        specialization: str,
        departament_id: int,
    ) -> None:
        super().__init__(id, name, surname, middle_name, birth_date, geo, contract)
        self.specialization = specialization
        self.departament_id = departament_id

    def get_info(self) -> str:
        return f"Это врач: {self.surname} {self.name} {self.middle_name}.\nСпециализация: {self.specialization}.\nРаботает в {self.departament_id} отделении."


class Inventory:
    def __init__(self, id: int, item: str) -> None:
        self.id = id
        self.item = item

    def get_info(self) -> str:
        return f"Это инвентарь. Содержимое инвентаря: {self.item}."


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
        dubinka: int,
    ) -> None:
        super().__init__(id, name, surname, middle, birth_date, geo, contract)
        self.dubinka = dubinka

    def get_info(self) -> str:
        return f"Это охранник - {self.surname} {self.name} {self.middle_name}.\nДата рождения: {self.birth_date}.\nМесто проживания: {self.geo}.\nКонтракт: {self.contract}.\nОборонительное оружие: {self.dubinka}"


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
    ) -> None:
        super().__init__(id, name, surname, middle_name, birth_date, geo)
        self.number_phone = number_phone

    def get_info(self) -> str:
        return f"Пациент - {self.surname} {self.name} {self.middle_name}.\nДата рождения: {self.birth_date}.\nМесто проживания: {self.geo}.\nНомер телефона: {self.number_phone}."


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


class Diagnosis:
    def __init__(self, id: int, number_mkb: str, description: str) -> None:
        self.id = id
        self.number_mkb = number_mkb
        self.description = description

    def get_info(self) -> str:
        return f"Диагноз №{self.number_mkb}.\nРасшифровка: {self.description}."


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


# кабинеты
class Rooms:
    def __init__(self, id: int, number_room: str, department_id: int) -> None:
        self.id = id
        self.number_room = number_room
        self.department_id = department_id

    def get_info(self) -> str:
        return f"Комната №{self.number_room}.\nПринадлежит отделению: {self.department_id}."


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
    ) -> None:
        self.adress = adress
        self.patient = patient
        self.doctor = doctor
        self.record = record
        self.employe = employe
        self.room = room
        self.department = department

    def get_patient(self, id: int):
        for item in self.patient:
            if id == item.id:
                return item

    def add_patient(self, patient: Patient) -> None:
        self.patient.append(patient)

    def update_patient(self, id: int, **kwargs) -> None:
        patient = self.get_patient(id)

        for key, value in kwargs.items():
            setattr(patient, key, value)

    def delete_patient(self, id: int) -> None:
        patient = self.get_patient(id)

        self.patient.remove(patient)

    def get_doctor(self, id: int):
        for item in self.doctor:
            if item.id == id:
                return item

    def add_doctor(self, doctor: Doctor) -> None:
        self.doctor.append(doctor)

    def update_doctor(self, id: int, **kwargs) -> None:
        doctor = self.get_doctor(id)

        for key, value in kwargs.items():
            setattr(doctor, key, value)

    def delete_doctor(self, id: int) -> None:
        doctor = self.get_doctor(id)

        self.doctor.remove(doctor)

    def get_record(self, id: int):
        for item in self.record:
            if item.id == id:
                return item

    def add_record(self, record: Record) -> None:
        self.record.append(record)

    def update_record(self, id: int, **kwargs) -> None:
        record = self.get_record(id)

        for key, value in kwargs.items():
            setattr(record, key, value)

    def delete_record(self, id: int) -> None:
        record = self.get_record(id)

        self.record.remove(record)

    def get_employe(self, id: int):
        for item in self.employe:
            if item.id == id:
                return item

    def add_employe(self, employe: Employ) -> None:
        self.employe.append(employe)

    def update_employe(self, id: int, **kwargs) -> None:
        employe = self.get_employe(id)

        for key, value in kwargs.items():
            setattr(employe, key, value)

    def delete_employe(self, id: int) -> None:
        employe = self.get_employe(id)

        self.employe.remove(employe)

    def get_room(self, id: int) -> Rooms:
        for item in self.room:
            if item.id == id:
                return item

    def update_room(self, id: int, **kwargs) -> None:
        room = self.get_room(id)

        for key, value in kwargs.items():
            setattr(room, key, value)

    def get_department(self, id: int) -> Departments:
        for item in self.department:
            if item.id == id:
                return item

    def update_department(self, id: int, **kwargs) -> None:
        department = self.get_department(id)

        for key, value in kwargs.items():
            setattr(department, key, value)

    @staticmethod
    def from_json(path) -> "Clinic":
        with open(path, "r") as file:
            res = json.load(file)

            for key, value in res.items():
                if isinstance(value, list):
                    for item in range(len(value)):
                        if key == 'patient':
                            value[item] = Patient(**value[item])
                        elif key == 'doctor':
                            value[item] = Doctor(**value[item])
                        # + rooms и тд  (сделать для всех)!
        return Clinic(**res)


    def to_json(self, path) -> None:
        data = {
            "adress": self.adress,
            "patient": [item.__dict__ for item in self.patient],
            "doctor": [item.__dict__ for item in self.doctor],
            "record": [item.__dict__ for item in self.record],
            "employe": [item.__dict__ for item in self.employe],
            "room": [item.__dict__ for item in self.room],
            "department": [item.__dict__ for item in self.department],
        }

        with open(path, "w") as file:
            json.dump(data, file, ensure_ascii=False)

    @staticmethod
    def from_xml(cls, path) -> None:
        pass

    def to_xml(self, path) -> None:

        # Создаем корневой элемент
        root = ET.Element("Clinica")
        ET.SubElement(root, "adress").text = str(self.adress)

        # для списков
        c_elem = ET.SubElement(root, "patients")
        for b_obj in self.patient:
            b_obj_elem = ET.SubElement(c_elem, "patient")
            ET.SubElement(b_obj_elem, "id").text = str(b_obj.id)
            ET.SubElement(b_obj_elem, "name").text = str(b_obj.name)
            ET.SubElement(b_obj_elem, "surname").text = str(b_obj.surname)
            ET.SubElement(b_obj_elem, "middle_name").text = str(b_obj.middle_name)
            ET.SubElement(b_obj_elem, "birth_date").text = str(b_obj.birth_date)
            ET.SubElement(b_obj_elem, "geo").text = str(b_obj.geo)
            ET.SubElement(b_obj_elem, "number_phone").text = str(b_obj.number_phone)
        # Далее для всех этих типа классов из клиники
        tree = ET.ElementTree(root)
        tree.write(path, encoding="utf-8", xml_declaration=True)


ivan = Doctor(
    1, "Ivan", "Ivanin", "Ivanovich", "21.06.2003", "Mahachkala", "23", "hz", 52
)
matrena = Patient(
    1, "Matrena", "Matrenina", "Vladislavovna", "13.02.2004", "Derbent", "+79002001000"
)
medsi = Clinic("Moskva", [matrena], [ivan], [], [], [], [])
medsi.to_json("example.json")
medsi1 = Clinic.from_json("example.json")
medsi1.to_xml("example.xml")
#print(medsi1.adress)