class Rectangle:

    def init(self):
        self.length = 1
        self.width = 1

    def set_width(self, width):
        self.width = width

    def set_length(self, length):
        self.length = length

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_area(self):
        return self.length * self.width

    def str(self):
        return 'length = {}, width = {}'.format(self.length, self.width)