from abc import ABC
from abc import abstractmethod
import json
import re

"""Deserialization json_files"""
try:
    with open("courses.json") as courseFile:
        dataCourses = json.load(courseFile)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')

try:
    with open("teachers.json") as teacherFile:
        dataTeachers = json.load(teacherFile)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')

"""Base interface classes"""


class ITeacher(ABC):
    @abstractmethod
    def __str__(self):
        pass


class ICourse(ABC):
    @abstractmethod
    def __str__(self):
        pass


class ICourseFactory:
    @abstractmethod
    def factoryCourse(self) -> ICourse: pass

    @abstractmethod
    def factoryTeacher(self, name) -> ITeacher: pass


"""Derived interface classes"""


class Teacher(ITeacher):
    """Class Teacher"""

    def __init__(self, name, qualification, phone):
        self.name = name
        self.qualification = qualification
        self.phone = phone
        self.course = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        self.__name = name

    @property
    def qualification(self):
        return self.__qualification

    @qualification.setter
    def qualification(self, qualification):
        if not isinstance(qualification, str):
            raise TypeError("Qualification must be str")
        self.__qualification = qualification

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, int):
            raise TypeError('The mobile phone must be type int')
        if not re.match(r"^(\+380|380)(\d{9})$", str(phone)):
            raise ValueError('Incorrect data.')
        self.__phone = phone

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        if not all(isinstance(courses, (OffsiteCourse, LocalCourse)) for courses in course):
            raise TypeError("Wrong type")
        self.__course = course

    def addCourse(self, courses):
        self.course.append(courses)


    def __str__(self):
        return f"Teacher:{self.name}\tQualification: {self.qualification}\tPhone: {self.phone}"


class Course(ICourse):
    """Class Course"""

    def __init__(self, title, program, description):
        self.title = title
        self.program = program
        self.description = description

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title course must be str")

        self.__title = title

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not all((prog, str) for prog in program):
            raise TypeError("Program course must be str")
        self.__program = program

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description course must be str")
        self.__description = description

    def __str__(self):
        return f"Course: {self.title}\t{self.program}"


class ILocalCourse(ABC):
    def __str__(self):
        pass


class IOffsiteCourse(ABC):
    def __str__(self):
        pass


class LocalCourse(Course, ILocalCourse):
    """Class LocalCourse subclass Course """
    def __str__(self):
        return f"\nLocal course:\t{self.title}\n\t\tProgram:{self.program}\n\t\tDescription:{self.description}"


class OffsiteCourse(Course, IOffsiteCourse):
    """Class OffsiteCourse subclass Course """
    def __str__(self):
        return f"\nOffsite course: {self.title}\n\t\tProgram{self.program}\n\t\t Description:{self.description}"


class CourseFactory(ICourseFactory):
    def factoryTeacher(self, numberTeather) -> ITeacher:
        nameTeacher = dataTeachers[numberTeather]["name"]
        qualification = dataTeachers[numberTeather]["qualification"]
        phone = dataTeachers[numberTeather]["phone"]
        return Teacher(nameTeacher,qualification,phone)

    def factoryCourse(self, nameCourse) -> ICourse:
        type = dataCourses[nameCourse]["type"]
        program = dataCourses[nameCourse]["program"]
        description = dataCourses[nameCourse]["description"]
        dictCourse={
            "LocalCourse":LocalCourse(nameCourse,program,description),
            "OffsiteCourse":OffsiteCourse(nameCourse,program,description)
        }
        return dictCourse[type]

    def TeacherCourses(self,numberTeacher,course):
        return f"{self.factoryTeacher(numberTeacher)}{self.factoryCourse(course)}"




f = CourseFactory()
teacher = f.factoryTeacher("1")
# print(teacher)
course1 = f.factoryCourse("SQL for all")
course2=f.factoryCourse("Python Programming")
# print(course1)
# print(course2)
print(f.TeacherCourses("1","Python Programming"))
