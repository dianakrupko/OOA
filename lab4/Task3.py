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
    def createTeacher(self):
        pass


class ICourse(ABC):
    @abstractmethod
    def createCourse(self):
        pass


class ICourseFactory:
    @abstractmethod
    def factoryCourse(self, courseTitle):
        pass

    @abstractmethod
    def factoryTeacher(self, teacherName):
        pass


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

    def createTeacher(self):
        return f"Teacher:{self.name}\tQualification: {self.qualification}\tPhone: {self.phone}"

    def __str__(self):
        res = ""
        for courses in self.course:
            res += courses.title + '\n\t\t'
        return f"Teacher:{self.name}\nCourse: {res}"


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

    def createCourse(self):
        return f"Course: {self.title}\t{self.program}"


class LocalCourse(Course):
    """Class LocalCourse subclass Course """

    def __init__(self, title, program, description):
        super().__init__(title, program, description)

    def createCourse(self):
        return f"Local:\t{self.title}\n\t\tProgram:{self.program}\n\t\tDescription:{self.description}"


class OffsiteCourse(Course):
    """Class OffsiteCourse subclass Course """

    def __init__(self, title, program, description):
        super().__init__(title, program, description)

    def createCourse(self):
        return f"Offsite: {self.title}\n\t\tProgram{self.program}\n\t\t Description:{self.description}"


class CourseFactory(ICourseFactory):
    """Class CourseFactory"""

    def factoryCourse(self, courseTitle):
        for course in dataCourses:
            if courseTitle == course["title"]:
                takenCourse = course
        dictCour = {
            "LocalCourse": LocalCourse,
            "OffsiteCourse": OffsiteCourse
        }
        return dictCour[takenCourse["type"]](takenCourse["title"], takenCourse["program"], takenCourse["description"])

    def factoryTeacher(self, teacherName):
        for teacher in dataTeachers:
            if teacherName == teacher["name"]:
                takenTeacher = teacher
        return Teacher(takenTeacher["name"], takenTeacher["qualification"], takenTeacher["phone"])


def add(teacher, courses):
    courses.teacher = teacher
    teacher.addCourse(courses)


f = CourseFactory()
teacher = f.factoryTeacher("Diana Krupko")
course_1 = f.factoryCourse("Python Programming")
course_2 = f.factoryCourse("SQL for all")
print(teacher.createTeacher())
print(course_2.createCourse())
print("=" * 150)
add(teacher, course_1)
add(teacher, course_2)
print(teacher)
