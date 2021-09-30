class Rectangle:

    def init(self):
        self.length = 1
        self.width = 1

    def set_width(self, width):
        self.width = width
        if not type(self.width) is float or self.width < 0.0 or self.width > 20.0:
            print("Error")

    def set_length(self, length):
        self.length = length
        if not type(self.length) is float or self.length < 0.0 or self.length > 20.0:
            print("Error")

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def str(self):
        return 'length = {}, width = {}'.format(self.length, self.width)
