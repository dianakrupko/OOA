import math
import sys

from fractions import Fraction


class Rational:

    def __init__(self, top=1, bottom=1):
        if not isinstance(top, int):
            raise TypeError('Top must be int')
        if not isinstance(bottom, int):
            raise TypeError('Bottom must be int')
        if not bottom:
            raise ZeroDivisionError
        divisor = math.gcd(top, bottom)
        self.__top = top // divisor
        self.__bottom = bottom // divisor

    def show(self):
        return f'{self.__top}/{self.__bottom}'

    def division(self):
        return self.__top / self.__bottom


a = Rational(2, 10)
print(a.show())
print(a.division())
