class Rectangle:

    def __init__(self, width=1, length=1):
        if not isinstance(width, float) or not isinstance(length, float):
            raise TypeError('Width and length must be float')
        if width < 0.0 or width > 20.0 or length < 0.0 or length > 20.0:
            raise ValueError('0.0 < width > 20.0 and 0.0 < length > 20.0')
        self.width = width
        self.length = length

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def str(self):
        return 'Width: {} \nLength: {}'.format(self.length, self.width)


r = Rectangle(5.2, 9.5)
# print(r.get_width())
# print(r.get_length())
print(r.str())
print("Area:", r.get_area())
print("Perimeter:", r.get_perimeter())
