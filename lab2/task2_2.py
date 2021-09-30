import math
from fractions import Fraction


class Rational:

    def __init__(self, top=1, bottom=1):
        self.__top = top
        self.__bottom = bottom
        if type(self.__top) is int and type(self.__bottom) is int:
            try:
                reduce_form = Fraction(self.__top, self.__bottom)
            except ZeroDivisionError:
                print("divided by zero")
                quit()
        else:
            print("incorrectly entered values")

    def show(self):
        print(self.__top, "/", self.__bottom)

    def division(self):
        return self.__top / self.__bottom


a = Rational(1, 5)
a.show()
print(a.division())
