from typing import List, Optional
import json
import xml.etree.ElementTree as ET
from Classes.Doctor import Doctor
from Classes.Employe import Employe
from Classes.Patient import Patient
from Classes.Departments import Departments
from Classes.Record import Record
from Classes.Rooms import Rooms
from Classes.Exceptions import (
    PatientNotFoundException,
    PatientNotUpdateException,
    PatientAlreadyExistsException,
    DoctorNotFoundException,
    DoctorNotUpdateException,
    DoctorAlreadyExistsException,
    DepartmentNotFoundException,
    DepartmentNotUpdateException,
    EmployeNotFoundException,
    EmployeAlreadyExistsException,
    EmployeNotUpdateException,
    RoomNotFoundException,
    RoomNotUpdateException,
    RecordNotUpdateException,
    RecordNotFoundException,
    RecordAlreadyExistsException,
    DuplicateException,
)


class Clinic:
    """Класс, представляющий поликлинику.
    Содержит информацию о пациентах, врачах, записях, сотрудниках, кабинетах и отделениях."""

    def __init__(
        self,
        adress: str,
        patient: List[Patient],
        doctor: List[Doctor],
        record: List[Record],
        employe: List[Employe],
        room: List[Rooms],
        department: List[Departments],
    ) -> None:
        """Инициализация атрибутов поликлиники"""
        self.adress = adress
        self.patient = patient
        self.doctor = doctor
        self.record = record
        self.employe = employe
        self.room = room
        self.department = department

        # проверка уникальности id при создании
        self._validate_unique_ids()

    def _validate_unique_ids(self) -> None:
        """Проверяет уникальность ID всех сущностей"""
        ids_seen = set()

        for entity_list, entity_name in [
            (self.patient, "Patient"),
            (self.doctor, "Doctor"),
            (self.record, "Record"),
            (self.employe, "Employe"),
            (self.room, "Rooms"),
            (self.department, "Department"),
        ]:
            for entity in entity_list:
                if entity.id in ids_seen:
                    raise DuplicateException(
                        f"Дублирущийся id {entity.id} для сущности {entity_name}"
                    )
                ids_seen.add(entity.id)

    def _check_entity_exists(self, entity_list: List, entity_id: int) -> bool:
        """Проверяет существование сущности по id"""
        return any(entity.id == entity_id for entity in entity_list)

    def get_patient(self, id: int) -> Patient:
        """Возвращает пациента по id"""
        for item in self.patient:
            if id == item.id:
                return item
        raise PatientNotFoundException(f"Пациент id={id} не найден!")

    def add_patient(self, patient: Patient) -> None:
        """Добавление нового пациента"""
        if self._check_entity_exists(self.patient, patient.id):
            raise PatientAlreadyExistsException(
                f"Пациент с id={patient.id} уже существует!"
            )
        self.patient.append(patient)

    def update_patient(self, id: int, **kwargs) -> None:
        """Обновление данных о пациентах"""
        patient = self.get_patient(id)
        original_values = {key: getattr(patient, key) for key in kwargs.keys()}

        for key, value in kwargs.items():
            setattr(patient, key, value)

        updated_values = {key: getattr(patient, key) for key in kwargs.keys()}
        if original_values == updated_values:
            raise PatientNotUpdateException(
                f"Ошибка! Не получилось обновить данные пациента с id={id}"
            )

    def delete_patient(self, id: int) -> None:
        """Удаление пациента по id"""
        patient = self.get_patient(id)
        self.patient.remove(patient)

    def get_doctor(self, id: int) -> Doctor:
        """Возвращает доктора по id"""
        for item in self.doctor:
            if item.id == id:
                return item
        raise DoctorNotFoundException(f"Врач id={id} не найден!")

    def add_doctor(self, doctor: Doctor) -> None:
        """Добавление нового доктора"""
        if self._check_entity_exists(self.doctor, doctor.id):
            raise DoctorAlreadyExistsException(f"Врач с id={doctor.id} уже сущестует!")
        self.doctor.append(doctor)

    def update_doctor(self, id: int, **kwargs) -> None:
        """Обновление данных о докторе"""
        doctor = self.get_doctor(id)
        original_values = {key: getattr(doctor, key) for key in kwargs.keys()}

        for key, value in kwargs.items():
            setattr(doctor, key, value)

        updated_values = {key: getattr(doctor, key) for key in kwargs.keys()}
        if original_values == updated_values:
            raise DoctorNotUpdateException(
                f"Ошибка! Не получилось обновить данные врача с id={id}"
            )

    def delete_doctor(self, id: int) -> None:
        """Удаление доктора по id"""
        doctor = self.get_doctor(id)
        self.doctor.remove(doctor)

    def get_record(self, id: int) -> Record:
        """Возвращает запись по id"""
        for item in self.record:
            if item.id == id:
                return item
        raise RecordNotFoundException(f"Запись id={id} не найдена!")

    def add_record(self, record: Record) -> None:
        """Добавление новой записи (на примем к врачу)"""
        if self._check_entity_exists(self.record, record.id):
            raise RecordAlreadyExistsException(
                f"Запись с id={record.id} уже существует!"
            )
        self.record.append(record)

    def update_record(self, id: int, **kwargs) -> None:
        """Обновление данных по записи"""
        record = self.get_record(id)
        original_values = {key: getattr(record, key) for key in kwargs.keys()}

        for key, value in kwargs.items():
            setattr(record, key, value)

        updated_values = {key: getattr(record, key) for key in kwargs.keys()}
        if original_values == updated_values:
            raise RecordNotUpdateException(
                f"Ошибка! Не получилось обновить запись с id={id}"
            )

    def delete_record(self, id: int) -> None:
        """Удаление записи"""
        record = self.get_record(id)
        self.record.remove(record)

    def get_employe(self, id: int) -> Employe:
        """Возвращает сотрудника по id"""
        for item in self.employe:
            if item.id == id:
                return item
        raise EmployeNotFoundException(f"Сотрудник id={id} не найден!")

    def add_employe(self, employe: Employe) -> None:
        """Добавление нового сотрудника"""
        if self._check_entity_exists(self.employe, employe.id):
            raise EmployeAlreadyExistsException(
                f"Сотрудник с id={employe.id} уже существует!"
            )
        self.employe.append(employe)

    def update_employe(self, id: int, **kwargs) -> None:
        """Обновление данных сотрудника"""
        employe = self.get_employe(id)
        original_values = {key: getattr(employe, key) for key in kwargs.keys()}

        for key, value in kwargs.items():
            setattr(employe, key, value)

        updated_values = {key: getattr(employe, key) for key in kwargs.keys()}
        if original_values == updated_values:
            raise EmployeNotUpdateException(
                f"ОшибкаЙ Не получилось обновить данные сотрудника с id={id}"
            )

    def delete_employe(self, id: int) -> None:
        """Удаление сотрудника"""
        employe = self.get_employe(id)
        self.employe.remove(employe)

    def get_room(self, id: int) -> Rooms:
        """Возвращает кабинет по id"""
        for item in self.room:
            if item.id == id:
                return item
        raise RoomNotFoundException(f"Комната id={id} не найдена!")

    def update_room(self, id: int, **kwargs) -> None:
        """Обновление данных по кабинету"""
        room = self.get_room(id)
        original_values = {key: getattr(room, key) for key in kwargs.keys()}

        for key, value in kwargs.items():
            setattr(room, key, value)

        updated_values = {key: getattr(room, key) for key in kwargs.keys()}
        if original_values == updated_values:
            raise RoomNotUpdateException(
                f"Ошибка! Не получилось обновить данные комнаты с id={id}"
            )

    def get_department(self, id: int) -> Departments:
        """Возвращает отделение по id"""
        for item in self.department:
            if item.id == id:
                return item
        raise DepartmentNotFoundException(f"Отделение id={id} не найдено!")

    def update_department(self, id: int, **kwargs) -> None:
        """Обновление данных об отделении"""
        department = self.get_department(id)
        original_values = {key: getattr(department, key) for key in kwargs.keys()}

        for key, value in kwargs.items():
            setattr(department, key, value)

        updated_values = {key: getattr(department, key) for key in kwargs.keys()}
        if original_values == updated_values:
            raise DepartmentNotUpdateException(
                f"Ошибка! Не получилось обновить данные отделения с id={id}"
            )

    @staticmethod
    def from_json(path) -> Optional["Clinic"]:
        """Создаёт объект Clinic из json-файл"""
        try:
            with open(path, "r") as file:
                res = json.load(file)
        except FileNotFoundError:
            print("Проверь название файла!")
            return None

        for key, value in res.items():
            if isinstance(value, list):
                for item in range(len(value)):
                    if key == "patient":
                        value[item] = Patient(**value[item])
                    elif key == "doctor":
                        value[item] = Doctor(**value[item])
                    elif key == "record":
                        value[item] = Record(**value[item])
                    elif key == "employe":
                        value[item] = Employe(**value[item])
                    elif key == "room":
                        value[item] = Rooms(**value[item])
                    elif key == "department":
                        value[item] = Departments(**value[item])
        return Clinic(**res)

    def to_json(self, path) -> None:
        """Сохраняет объект Clinic в json-файл"""
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
    def from_xml(path) -> "Clinic":
        """Создаёт объект Clinic из XML-файла"""
        tree = ET.parse(path)
        root = tree.getroot()

        adress = root.find("adress").text

        patient = []
        doctor = []
        record = []
        employe = []
        rooms = []
        department = []
        elem_patient = root.find("patients")
        for item in elem_patient.findall("patient"):
            id = int(item.find("id").text)
            name = str(item.find("name").text)
            surname = str(item.find("surname").text)
            middle_name = str(item.find("middle_name").text)
            birth_date = str(item.find("birth_date").text)
            geo = str(item.find("geo").text)
            number_phone = str(item.find("number_phone").text)

            pat = Patient(
                id=id,
                name=name,
                surname=surname,
                middle_name=middle_name,
                birth_date=birth_date,
                geo=geo,
                number_phone=number_phone,
            )

            patient.append(pat)

        elem_doctor = root.find("doctor")
        for item in elem_doctor.findall("doctor"):
            id = int(item.find("id").text)
            name = str(item.find("name").text)
            surname = str(item.find("surname").text)
            middle_name = str(item.find("middle_name").text)
            birth_date = str(item.find("birth_date").text)
            geo = str(item.find("geo").text)
            contract = str(item.find("contract").text)
            specialization = str(item.find("specialization").text)
            department_id = int(item.find("department_id").text)

            doc = Doctor(
                id=id,
                name=name,
                surname=surname,
                middle_name=middle_name,
                birth_date=birth_date,
                geo=geo,
                contract=contract,
                specialization=specialization,
                department_id=department_id,
            )

            doctor.append(doc)

        elem_record = root.find("record")
        for item in elem_record.findall("record"):
            id = int(item.find("id").text)
            patient_id = int(item.find("patient_id").text)
            diagnosis_ids = [int(i) for i in item.find("diagnosis_ids").text.split(",")]
            doctor_id = int(item.find("doctor_id").text)
            data = str(item.find("data").text)
            recipe_ids = [int(i) for i in item.find("recipe_ids").text.split(",")]

            rec = Record(
                id=id,
                patient_id=patient_id,
                diagnosis_ids=diagnosis_ids,
                doctor_id=doctor_id,
                data=data,
                recipe_ids=recipe_ids,
            )

            record.append(rec)

        elem_employe = root.find("employe")
        for item in elem_employe.findall("employe"):
            id = int(item.find("id").text)
            name = str(item.find("name").text)
            surname = str(item.find("surname").text)
            middle_name = str(item.find("middle_name").text)
            birth_date = str(item.find("birth_date").text)
            geo = str(item.find("geo").text)
            contract = str(item.find("contract").text)

            epl = Employe(
                id=id,
                name=name,
                surname=surname,
                middle_name=middle_name,
                birth_date=birth_date,
                geo=geo,
                contract=contract,
            )

            employe.append(epl)

        elem_room = root.find("room")
        for item in elem_room.findall("room"):
            id = int(item.find("id").text)
            number_room = str(item.find("number_room").text)
            department_id = int(item.find("department_id").text)

            room = Rooms(
                id=id,
                number_room=number_room,
                department_id=department_id,
            )

            rooms.append(room)

        elem_department = root.find("department")
        for item in elem_department.findall("department"):
            id = int(item.find("id").text)
            name = str(item.find("name").text)

            dprt = Departments(
                id=id,
                name=name,
            )

            department.append(dprt)

        return Clinic(adress, patient, doctor, record, employe, rooms, department)

    def to_xml(self, path) -> None:
        """Сохраняем объект Clinic в XML-файл"""

        # Создаем корневой элемент
        root = ET.Element("Clinica")
        ET.SubElement(root, "adress").text = str(self.adress)

        # для списков
        elem_patient = ET.SubElement(root, "patients")
        for obj in self.patient:
            obj_elem = ET.SubElement(elem_patient, "patient")
            ET.SubElement(obj_elem, "id").text = str(obj.id)
            ET.SubElement(obj_elem, "name").text = str(obj.name)
            ET.SubElement(obj_elem, "surname").text = str(obj.surname)
            ET.SubElement(obj_elem, "middle_name").text = str(obj.middle_name)
            ET.SubElement(obj_elem, "birth_date").text = str(obj.birth_date)
            ET.SubElement(obj_elem, "geo").text = str(obj.geo)
            ET.SubElement(obj_elem, "number_phone").text = str(obj.number_phone)

        elem_doctor = ET.SubElement(root, "doctor")
        for obj in self.doctor:
            obj_elem = ET.SubElement(elem_doctor, "doctor")
            ET.SubElement(obj_elem, "id").text = str(obj.id)
            ET.SubElement(obj_elem, "name").text = str(obj.name)
            ET.SubElement(obj_elem, "surname").text = str(obj.surname)
            ET.SubElement(obj_elem, "middle_name").text = str(obj.middle_name)
            ET.SubElement(obj_elem, "birth_date").text = str(obj.birth_date)
            ET.SubElement(obj_elem, "geo").text = str(obj.geo)
            ET.SubElement(obj_elem, "contract").text = str(obj.contract)
            ET.SubElement(obj_elem, "specialization").text = str(obj.specialization)
            ET.SubElement(obj_elem, "department_id").text = str(obj.department_id)

        elem_record = ET.SubElement(root, "record")
        for obj in self.record:
            obj_elem = ET.SubElement(elem_record, "record")
            ET.SubElement(obj_elem, "id").text = str(obj.id)
            ET.SubElement(obj_elem, "patient_id").text = str(obj.patient_id)
            ET.SubElement(obj_elem, "diagnosis_ids").text = ",".join(
                str(id) for id in obj.diagnosis_ids
            )
            ET.SubElement(obj_elem, "doctor_id").text = str(obj.doctor_id)
            ET.SubElement(obj_elem, "data").text = str(obj.data)
            ET.SubElement(obj_elem, "recipe_ids").text = ",".join(
                str(id) for id in obj.recipe_ids
            )

        elem_employe = ET.SubElement(root, "employe")
        for obj in self.employe:
            obj_elem = ET.SubElement(elem_employe, "employe")
            ET.SubElement(obj_elem, "id").text = str(obj.id)
            ET.SubElement(obj_elem, "name").text = str(obj.name)
            ET.SubElement(obj_elem, "surname").text = str(obj.surname)
            ET.SubElement(obj_elem, "middle_name").text = str(obj.middle_name)
            ET.SubElement(obj_elem, "birth_date").text = str(obj.birth_date)
            ET.SubElement(obj_elem, "geo").text = str(obj.geo)
            ET.SubElement(obj_elem, "contract").text = str(obj.contract)

        elem_room = ET.SubElement(root, "room")
        for obj in self.room:
            obj_elem = ET.SubElement(elem_room, "room")
            ET.SubElement(obj_elem, "id").text = str(obj.id)
            ET.SubElement(obj_elem, "number_room").text = str(obj.number_room)
            ET.SubElement(obj_elem, "department_id").text = str(obj.department_id)

        elem_department = ET.SubElement(root, "department")
        for obj in self.department:
            obj_elem = ET.SubElement(elem_department, "department")
            ET.SubElement(obj_elem, "id").text = str(obj.id)
            ET.SubElement(obj_elem, "name").text = str(obj.name)

        tree = ET.ElementTree(root)
        tree.write(path, encoding="utf-8", xml_declaration=True)
