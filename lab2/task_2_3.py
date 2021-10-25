import re  # for function match


class Student:
    """The class describes the student"""

    def __init__(self, name, surname, gradebook, score):
        """
        Initializes all necessary attributes in Student
        :param name: str, name student
        :param surname:str, surname student
        :param gradebook:str, number gradebook student
        :param score:dict, score student
        """
        self.name = name
        self.surname = surname
        self.gradebook = gradebook
        self.score = score

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name):
            if not name.isalpha():
                raise ValueError('The name consists of letters')
            self.__name = name

        @property
        def surname(self):
            return self.__surname

        @name.setter
        def surname(self, surname):
            if not surname.isalpha():
                raise ValueError('The surname consists of letters')
            self.__surname = surname

        @property
        def gradebook(self):
            return self.__gradebook

        @gradebook.setter
        def gradebook(self, gradebook):
            if not re.match(r'^[A-Z]{2}[-][0-9]{5}', str(gradebook)):
                raise ValueError('Incorrect data.Gradebook XX-_____')
            self.__gradebook = gradebook

        @property
        def score(self):
            return self.__score

        @score.setter
        def score(self, score):
            if not all([isinstance(x, int) for x in score.values()]):
                raise TypeError("Wrong type")
            if not all([60 <= x <= 100 for x in score.values()]):
                raise ValueError('Incorrect data.Values=[60;100]')
            self.__score = score

    # The function returns the averege
    def getAverage(self):
        self.b = list(self.score.values())
        sum = 0
        for i in self.b:
            sum = sum + i
        return sum / len(self.b)

    # Value check function
    def __lt__(self, other):
        return self.getAverage() > other.getAverage()

    def __str__(self):
        """Return information about student in one string."""
        return f"{self.name} \t{self.surname} \t{self.gradebook} \t" \
               f"{self.score} \t{self.getAverage()}"


class Group:
    """The class describes the group"""

    def __init__(self, students):
        """
        Initializes all necessary attributes in Group
        :param students: list, all students in the group
        """
        if not all([isinstance(s, Student) for s in students]):
            raise TypeError("Wrong type")
        if len(students) > 20:
            raise OverflowError("Lots of students")
        self.students = students

    # Adding a student to a group
    def addStudent(self, student):
        if not isinstance(student, Student):
            raise TypeError('Wrong type')
        self.students.append(student)

    # The function removes the student from the group
    def delStudent(self, student):
        if not isinstance(student, Student):
            raise TypeError('Wrong type')
        self.students.remove(student)

    def topStudent(self):
        """Display to cons ole the top 5 students by average grade."""
        self.students = sorted(self.students, reverse=False)
        return self.students[:5]


S1 = Student("Diana", "K", "TM-74320",
             {"Language": 60, 'Math': 78, 'Physics': 50, "Chemical": 80})
S2 = Student("Dima", "L", "TM-74326",
             {"Language": 90, 'Math': 70, 'Physics': 80, "Chemical": 60})
S3 = Student("Ira", "K", "TM-43215",
             {"Language": 100, 'Math': 70, 'Physics': 90, "Chemical": 65})
S4 = Student("Petya", "S", "TM-74360",
             {"Language": 90, 'Math': 90, 'Physics': 79, "Chemical": 88})
S5 = Student("Sofia", "J", "TM-74370",
             {"Language": 100, 'Math': 97, 'Physics': 70, "Chemical": 60})
S6 = Student("Ivanna", "K", "TM-74328",
             {"Language": 100, 'Math': 100, 'Physics': 100, "Chemical": 95})
S7 = Student("Kate", "V", "TM-74324",
             {"Language": 70, 'Math': 87, 'Physics': 79, "Chemical": 70})
S8 = Student("Vicky", "L", "TM-74345",
             {"Language": 90, 'Math': 90, 'Physics': 70, "Chemical": 60})
S9 = Student("Nikita", "M", "TM-74354",
             {"Language": 100, 'Math': 100, 'Physics': 71, "Chemical": 100})
S10 = Student("Miky", "B", "TM-74378",
              {"Language": 72, 'Math': 90, 'Physics': 100, "Chemical": 60, "Logic": 100})
gr = Group({S1, S2, S3, S4, S5, S6, S7, S8, S10})
for student in gr.topStudent():
    print(student)
gr.addStudent(S9)
gr.delStudent(S8)

