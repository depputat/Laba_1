from typing import List
import json
import xml.etree.ElementTree as ET
from Doctor import Doctor
from Employe import Employe
from Patient import Patient
from Departments import Departments
from Record import Record
from Rooms import Rooms


class Clinic:
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

    def add_employe(self, employe: Employe) -> None:
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
            diagnosis_ids = [int(diag.text) for diag in item.find("diagnosis_ids")] # вопросик
            doctor_id = int(item.find("doctor_id").text)
            data = str(item.find("data").text)

            rec = Record(
                id=id,
                patient_id=patient_id,
                diagnosis_ids=diagnosis_ids,
                doctor_id=doctor_id,
                data=data,
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
            ET.SubElement(obj_elem, "id").text = int(obj.id)
            ET.SubElement(obj_elem, "name").text = str(obj.name)
            ET.SubElement(obj_elem, "surname").text = str(obj.surname)
            ET.SubElement(obj_elem, "middle_name").text = str(obj.middle_name)
            ET.SubElement(obj_elem, "birth_date").text = str(obj.birth_date)
            ET.SubElement(obj_elem, "geo").text = str(obj.geo)
            ET.SubElement(obj_elem, "contract").text = str(obj.contract)
            ET.SubElement(obj_elem, "specialization").text = str(obj.specialization)
            ET.SubElement(obj_elem, "department_id").text = int(obj.department_id)

        elem_record = ET.SubElement(root, "record")
        for obj in self.record:
            obj_elem = ET.SubElement(elem_record, "record")
            ET.SubElement(obj_elem, "id").text = int(obj.id)
            ET.SubElement(obj_elem, "patient_id").text = int(obj.patient_id)
            ET.SubElement(obj_elem, "diagnosis_ids").text = ','.join(str(id) for id in obj.diagnosis_ids) # вопросик
            ET.SubElement(obj_elem, "doctor_id").text = int(obj.doctor_id)
            ET.SubElement(obj_elem, "data").text = str(obj.data)

        elem_employe = ET.SubElement(root, "employe")
        for obj in self.employe:
            obj_elem = ET.SubElement(elem_employe, "employe")
            ET.SubElement(obj_elem, "id").text = int(obj.id)
            ET.SubElement(obj_elem, "name").text = str(obj.name)
            ET.SubElement(obj_elem, "surname").text = str(obj.surname)
            ET.SubElement(obj_elem, "middle_name").text = str(obj.middle_name)
            ET.SubElement(obj_elem, "birth_date").text = str(obj.birth_date)
            ET.SubElement(obj_elem, "geo").text = str(obj.geo)
            ET.SubElement(obj_elem, "constract").text = str(obj.contract)

        elem_room = ET.SubElement(root, "room")
        for obj in self.room:
            obj_elem = ET.SubElement(elem_room, "room")
            ET.SubElement(obj_elem, "id").text = int(obj.id)
            ET.SubElement(obj_elem, "number_room").text = str(obj.number_room)
            ET.SubElement(obj_elem, "department_id").text = int(obj.department_id)

        elem_department = ET.SubElement(root, "department")
        for obj in self.department:
            obj_elem = ET.SubElement(elem_department, "department")
            ET.SubElement(obj_elem, "id").text = int(obj.id)
            ET.SubElement(obj_elem, "name").text = str(obj.name)


        tree = ET.ElementTree(root)
        tree.write(path, encoding="utf-8", xml_declaration=True)


ivan = Doctor(
    1, "Ivan", "Ivanin", "Ivanovich", "21.06.2000", "Mahachkala", "23", "hz", 52
)
matrena = Patient(
    1, "Matrena", "Matrenina", "Vladislavovna", "13.02.2004", "Derbent", "+79002001000"
)
medsi = Clinic("Moskva", [matrena], [ivan], [], [], [], [])
medsi.to_json("example.json")
medsi1 = Clinic.from_json("example.json")
medsi1.to_xml("example.xml")
kontora = Clinic.from_xml("example.xml")
#r = Patient.get_info(Clinic.get_patient(Clinic.from_xml("example.xml"), 1))
#print(r)
# print(kontora.adress)
# print(medsi1.adress)
