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
        if not name.isalpha():
            raise ValueError('Incorrect data')
        if not surname.isalpha():
            raise ValueError('Incorrect data')
        if not re.match(r'^[A-Z]{2}[-][0-9]{5}', str(gradebook)):
            raise ValueError('Incorrect data.Gradebook XX-_____')
        if not all([isinstance(x, int) for x in score.values()]):
            raise TypeError("Wrong type")
        if not all([60 <= x <= 100 for x in score.values()]):
            raise ValueError('Incorrect data.Values=[60;100]')
        self.name = name
        self.surname = surname
        self.gradebook = gradebook
        self.score = score

    # The function returns the name
    def get_name(self):
        return self.name

    # The function returns the surname
    def get_surname(self):
        return self.surname

    # The function returns the gradebook
    def get_gradebook(self):
        return self.gradebook

    # The function returns the averege
    def get_average(self):
        self.b = list(self.score.values())
        sum = 0
        for i in self.b:
            sum = sum + i
        return sum / len(self.b)

    # Value check function
    def __lt__(self, other):
        return self.get_average() > other.get_average()


class Group:
    """The class describes the group"""

    def __init__(self, *listst):
        """
        Initializes all necessary attributes in Group
        :param listst: list, all students in the group
        """
        if not all([isinstance(s, Student) for s in listst]):
            raise TypeError("Wrong type")
        self.listst = listst

    # The function of removing the first five students by rating
    def func(self):
        self.listst = sorted(self.listst)
        gr_stud = []
        for i in range(5):
            gr_stud.append(
                f'{self.listst[i].name} \t{self.listst[i].surname} \t{self.listst[i].gradebook} \t{self.listst[i].get_average()}\n')
        return "".join(gr_stud)


S1 = Student("Diana", "K", "TM-74329",
             {"Language": 60, 'Math': 78, 'Physics': 70, "Chemical": 80})
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
              {"Language": 72, 'Math': 90, 'Physics': 100, "Chemical": 60})
ob = Group(S1, S2, S3, S4, S5, S6, S7, S8, S10)
print(ob.func())
