# базовое исключение для клиники
class ClinicException(Exception):
    pass


# исключения для пациентов
class PatientNotFoundException(Exception):
    pass


class PatientNotUpdateException(Exception):
    pass


class PatientAlreadyExistsException(Exception):
    pass


# Исключения для докторов
class DoctorNotFoundException(Exception):
    pass


class DoctorNotUpdateException(Exception):
    pass


class DoctorAlreadyExistsException(Exception):
    pass


# Исключения для записей
class RecordNotFoundException(Exception):
    pass


class RecordNotUpdateException(Exception):
    pass


class RecordAlreadyExistsException(Exception):
    pass


# исключения для сотрудников
class EmployeNotFoundException(Exception):
    pass


class EmployeNotUpdateException(Exception):
    pass


class EmployeAlreadyExistsException(Exception):
    pass


# исключения для комнат
class RoomNotFoundException(Exception):
    pass


class RoomNotUpdateException(Exception):
    pass


# исключения для отделений
class DepartmentNotFoundException(Exception):
    pass


class DepartmentNotUpdateException(Exception):
    pass


# общие исключения для валидации
class InvalidDataException(ClinicException):
    pass


class DuplicateException(ClinicException):
    pass
