from math import gcd as compute_gcd


class Rational:
    """class Rational-class of rational numbers"""
    def __init__(self, numerator=0, denominator=1):
        """
        Initializes all necessary attributes in class Rational
        :param numerator:int, numerator of the fraction
        :param denominator:int, denominator of the fraction
        """
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError('Numerator must be int.')
        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError('Denominator must be int.')
        if denominator == 0:
            raise ZeroDivisionError('Division by zero')
        self.__denominator = denominator

    def reduce(self):
        gcd = compute_gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)

    def __add__(self, other):
        if type(other) == type(self):
            numerator = self.numerator * other.denominator + self.denominator * other.numerator
            denominator = self.denominator * other.denominator
        else:
            numerator = self.numerator + self.denominator * other
            denominator = self.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        if type(other) == type(self):
            numerator = self.numerator * other.denominator - self.denominator * other.numerator
            denominator = self.denominator * other.denominator
        else:
            numerator = self.numerator - self.denominator * other
            denominator = self.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        if type(other) == type(self):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
        else:
            numerator = self.numerator * other
            denominator = self.denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        if type(other) == type(self):
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
        else:
            numerator = self.numerator
            denominator = self.denominator * other
        return Rational(numerator, denominator)

    def __iadd__(self, other):
        if type(other) == type(self):
            self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
        else:
            self.numerator = self.numerator + self.denominator * other
        return self

    def __isub__(self, other):
        if type(other) == type(self):
            self.numerator = self.numerator * other.denominator - self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
        else:
            self.numerator = self.numerator - self.denominator * other
        return self

    def __imul__(self, other):
        if type(other) == type(self):
            self.numerator = self.numerator * other.numerator
            self.denominator = self.denominator * other.denominator
        else:
            self.numerator = self.numerator * other
        return self

    def __itruediv__(self, other):
        if type(other) == type(self):
            self.numerator = self.numerator * other.denominator
            self.denominator = self.denominator * other.numerator
        else:
            self.denominator = self.denominator * other
        return self

    def __lt__(self, other):
        if type(other) == type(self):
            if self.numerator * other.denominator < other.numerator * self.denominator:
                return True
            else:
                return False
        else:
            if self.numerator < other * self.denominator:
                return True
            else:
                return False

    def __le__(self, other):
        if type(other) == type(self):
            if self.numerator * other.denominator <= other.numerator * self.denominator:
                return True
            else:
                return False
        else:
            if self.numerator <= other * self.denominator:
                return True
            else:
                return False

    def __gt__(self, other):
        if type(other) == type(self):
            if self.numerator * other.denominator > other.numerator * self.denominator:
                return True
            else:
                return False
        else:
            if self.numerator > other * self.denominator:
                return True
            else:
                return False

    def __ge__(self, other):
        if type(other) == type(self):
            if self.numerator * other.denominator >= other.numerator * self.denominator:
                return True
            else:
                return False
        else:
            if self.numerator >= other * self.denominator:
                return True
            else:
                return False

    def __eq__(self, other):
        if type(other) == type(self):
            if self.numerator * other.denominator == other.numerator * self.denominator:
                return True
            else:
                return False
        else:
            if self.numerator == other * self.denominator:
                return True
            else:
                return False

    def __ne__(self, other):
        if type(other) == type(self):
            if self.numerator * other.denominator != other.numerator * self.denominator:
                return True
            else:
                return False
        else:
            if self.numerator != other * self.denominator:
                return True
            else:
                return False

    def __str__(self):
        if self.denominator == 1:
            return f'{self.numerator}'
        else:
            return "{}/{}".format(self.numerator, self.denominator)


a = Rational(3, 4)
b = Rational(2, 5)
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '>', b, '=', a > b)
print(a, '>=', b, '=', a >= b)
print(a, '<', b, '=', a < b)
print(a, '<=', b, '=', a <= b)
print(a, '==', b, '=', a == b)
print(a, '!=', b, '=', a != b)
# print(a, '+=', b, '=')
# a+=b
# print("\t\t\t",a)

# a*=b
# print(a, '*=', b, '=', a)
# a-=b
# print(a, '-=', b, '=', a)
# a/=b
# print(a, '+=', b, '/', a)

# a+=4
# print(a, '+=', 4, '=', a)
