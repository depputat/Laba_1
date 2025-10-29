from Classes.Clinic import Departments, Doctor, Employe, Patient, Rooms, Record, Clinic
from Classes.Exceptions import ClinicException, PatientNotUpdateException, PatientNotFoundException, PatientAlreadyExistsException


if __name__ == "__main__":
    try:
        # Создаем отделения (уникальные ID)
        dept_1 = Departments(1, "Терапия")
        dept_2 = Departments(2, "Хирургия")
        dept_3 = Departments(3, "Кардиология")

        # Создаем пациентов (уникальные ID, отличные от отделений)
        patient_1 = Patient(
            101,
            "Матрена",
            "Матренина",
            "Владиславовна",
            "13.02.2004",
            "Дербент",
            "+79002001000",
        )
        patient_2 = Patient(
            102, "Иван", "Иванов", "Петрович", "15.03.1980", "Москва", "+79003002000"
        )
        patient_3 = Patient(
            103,
            "Светлана",
            "Сидорова",
            "Александровна",
            "20.07.1995",
            "Казань",
            "+79004003000",
        )

        # Создаем врачей (уникальные ID)
        doctor_1 = Doctor(
            201,
            "Иван",
            "Иванин",
            "Иванович",
            "21.06.2000",
            "Махачкала",
            "контракт №23",
            "терапевт",
            1,
        )
        doctor_2 = Doctor(
            202,
            "Петр",
            "Петров",
            "Сергеевич",
            "10.05.1985",
            "Москва",
            "контракт №45",
            "хирург",
            2,
        )
        doctor_3 = Doctor(
            203,
            "Анна",
            "Каренина",
            "Владимировна",
            "30.11.1990",
            "Санкт-Петербург",
            "контракт №67",
            "кардиолог",
            3,
        )

        # Создаем записи (уникальные ID)
        record_1 = Record(301, 101, [1, 2], 201, "13.09.2024", [1, 2])
        record_2 = Record(302, 102, [3, 4], 202, "14.09.2024", [3, 4])
        record_3 = Record(303, 103, [5, 6], 203, "15.09.2024", [5, 6])

        # Создаем сотрудников (уникальные ID)
        employe_1 = Employe(
            401,
            "Ольга",
            "Семенова",
            "Дмитриевна",
            "05.08.1992",
            "Москва",
            "контракт №101",
        )
        employe_2 = Employe(
            402,
            "Сергей",
            "Кузнецов",
            "Анатольевич",
            "12.12.1988",
            "Казань",
            "контракт №102",
        )
        employe_3 = Employe(
            403, "Мария", "Попова", "Игоревна", "25.04.1995", "Сочи", "контракт №103"
        )

        # Создаем комнаты (уникальные ID)
        room_1 = Rooms(501, "101", 1)
        room_2 = Rooms(502, "201", 2)
        room_3 = Rooms(503, "301", 3)
        room_4 = Rooms(504, "102", 1)
        room_5 = Rooms(505, "202", 2)

        # Создаем клинику
        medsi = Clinic(
            "Москва, ул. Ленина, д. 25",
            [patient_1, patient_2, patient_3],
            [doctor_1, doctor_2, doctor_3],
            [record_1, record_2, record_3],
            [employe_1, employe_2, employe_3],
            [room_1, room_2, room_3, room_4, room_5],
            [dept_1, dept_2, dept_3],
        )

        print("Клиника успешно создана")

        # Тестируем функционал пациентов
        print("\n--- ТЕСТИРОВАНИЕ ПАЦИЕНТОВ ---")

        # Получаем пациента
        found_patient = medsi.get_patient(101)
        print(f"Найден пациент: {found_patient.name} {found_patient.surname}")

        # Обновляем пациента
        medsi.update_patient(101, name="Мария", geo="Москва")
        updated_patient = medsi.get_patient(101)
        print(
            f"Обновленный пациент: {updated_patient.name}, адрес: {updated_patient.geo}"
        )

        # Добавляем нового пациента
        new_patient = Patient(
            104,
            "Алексей",
            "Новиков",
            "Сергеевич",
            "10.10.1990",
            "Новосибирск",
            "+79005004000",
        )
        medsi.add_patient(new_patient)
        print(f"Добавлен новый пациент: {new_patient.name} {new_patient.surname}")

        # Тестируем функционал врачей
        print("\n--- ТЕСТИРОВАНИЕ ВРАЧЕЙ ---")

        found_doctor = medsi.get_doctor(201)
        print(
            f"Найден врач: {found_doctor.name} {found_doctor.surname}, специальность: {found_doctor.specialization}"
        )

        medsi.update_doctor(202, specialization="нейрохирург")
        updated_doctor = medsi.get_doctor(202)
        print(f"Обновленный врач: {updated_doctor.specialization}")

        # Тестируем функционал записей
        print("\n--- ТЕСТИРОВАНИЕ ЗАПИСЕЙ ---")

        found_record = medsi.get_record(301)
        print(
            f"Найдена запись: ID={found_record.id}, пациент ID={found_record.patient_id}"
        )

        medsi.update_record(301, diagnosis_ids=[1, 2, 7])
        updated_record = medsi.get_record(301)
        print(f"Обновленная запись: диагнозы {updated_record.diagnosis_ids}")

        # Тестируем функционал сотрудников
        print("\n--- ТЕСТИРОВАНИЕ СОТРУДНИКОВ ---")

        found_employe = medsi.get_employe(401)
        print(f"Найден сотрудник: {found_employe.name} {found_employe.surname}")

        medsi.update_employe(401, contract="контракт №201 (продлен)")
        updated_employe = medsi.get_employe(401)
        print(f"Обновленный контракт: {updated_employe.contract}")

        # Тестируем функционал комнат
        print("\n--- ТЕСТИРОВАНИЕ КОМНАТ ---")

        found_room = medsi.get_room(501)
        print(f"Найдена комната: №{found_room.number_room}")

        medsi.update_room(501, number_room="101-A")
        updated_room = medsi.get_room(501)
        print(f"Обновленная комната: №{updated_room.number_room}")

        # Тестируем функционал отделений
        print("\n--- ТЕСТИРОВАНИЕ ОТДЕЛЕНИЙ ---")

        found_dept = medsi.get_department(1)
        print(f"Найдено отделение: {found_dept.name}")

        medsi.update_department(1, name="Общая терапия")
        updated_dept = medsi.get_department(1)
        print(f"Обновленное отделение: {updated_dept.name}")

        # Сохраняем в JSON
        print("\n--- СОХРАНЕНИЕ В JSON ---")
        medsi.to_json("clinic_full_data.json")
        print("Данные сохранены в clinic_full_data.json")

        # Загружаем из JSON
        print("\n--- ЗАГРУЗКА ИЗ JSON ---")
        loaded_clinic = Clinic.from_json("clinic_full_data.json")
        print(f"Данные загружены. Адрес клиники: {loaded_clinic.adress}")
        print(f"Пациентов: {len(loaded_clinic.patient)}")
        print(f"Врачей: {len(loaded_clinic.doctor)}")
        print(f"Записей: {len(loaded_clinic.record)}")
        print(f"Сотрудников: {len(loaded_clinic.employe)}")
        print(f"Комнат: {len(loaded_clinic.room)}")
        print(f"Отделений: {len(loaded_clinic.department)}")

        # Тестируем исключения
        print("\n--- ТЕСТИРОВАНИЕ ИСКЛЮЧЕНИЙ ---")

        try:
            medsi.get_patient(999)  # Несуществующий ID
        except PatientNotFoundException as e:
            print(f"Корректно обработано: {e}")

        try:
            duplicate_patient = Patient(
                101, "Дубликат", "Дубликатов", "", "01.01.2000", "Город", "+79000000000"
            )
            medsi.add_patient(duplicate_patient)
        except PatientAlreadyExistsException as e:
            print(f"Корректно обработано: {e}")

        try:
            # Попытка обновления без изменений
            medsi.update_patient(102)  # Без параметров
        except PatientNotUpdateException as e:
            print(f"Корректно обработано: {e}")

        # Сохраняем в XML
        print("\n--- СОХРАНЕНИЕ В XML ---")
        medsi.to_xml("clinic_full_data.xml")
        print("Данные сохранены в clinic_full_data.xml")

        # Загружаем из XML
        print("\n--- ЗАГРУЗКА ИЗ XML ---")
        xml_clinic = Clinic.from_xml("clinic_full_data.xml")
        print(f"XML данные загружены. Адрес: {xml_clinic.adress}")
        print(
            f"Первый пациент: {xml_clinic.patient[0].name} {xml_clinic.patient[0].surname}"
        )

        # Демонстрация удаления
        print("\n--- ТЕСТИРОВАНИЕ УДАЛЕНИЯ ---")
        print(f"Пациентов до удаления: {len(medsi.patient)}")
        medsi.delete_patient(104)
        print(f"Пациентов после удаления: {len(medsi.patient)}")

        # Финальное сохранение
        medsi.to_json("clinic_final.json")
        print("\nФинальные данные сохранены в clinic_final.json")

        print("\nВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")

    except ClinicException as e:
        print(f"Ошибка клиники: {e}")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
