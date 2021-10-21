import math
import sys

from fractions import Fraction


class Rational:

    def __init__(self, top=1, bottom=1):
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise TypeError('Top and bottom must be int')
        if not bottom:
            raise ZeroDivisionError
        self.__top = top
        self.__bottom = bottom


    def show(self):
        return Fraction(self.__top, self.__bottom)

    def division(self):
        return self.__top / self.__bottom


a = Rational(2,10)
print(a.show())
print(a.division())
