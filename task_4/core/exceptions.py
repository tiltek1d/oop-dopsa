class SchoolException(Exception):
    ...


class SchoolSystemException(SchoolException):
    ...


class StudentException(SchoolException):
    ...


class TeacherException(SchoolException):
    ...


class AgeException(SchoolException):
    ...


class TeachersAgeException(AgeException, TeacherException):
    ...


class StudentsAgeException(AgeException, StudentException):
    ...


class AssignmentException(SchoolSystemException):
    ...


class NoSuitableTeacherException(AssignmentException):
    ...
