class Node:
    def __init__(self, key, price):
        """
        Initializes all necessary attributes in product
        :param key: int, product code
        :param price: int, price product
        """
        if not isinstance(key, int):
            raise TypeError('Key must be int.')
        if not isinstance(price, int):
            raise TypeError('Price must be int.')
        if key <= 0:
            raise ValueError('Key must be >0')
        if price <= 0:
            raise ValueError('Price must be >0')

        self.left = None
        self.right = None
        self.key = key
        self.price = price

    # Insert method to create nodes
    def insert(self, key, price):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key, price)
                else:
                    self.left.insert(key, price)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, price)
                else:
                    self.right.insert(key, price)
        else:
            self.key = key
            self.price = self.price

    #The method returns the price of the product through the key
    def func(self, key):
        if key < self.key:
            if not self.left:
                raise ValueError (str(key) + " Not Found")
            return self.left.func(key)
        elif key > self.key:
            if not self.right:
                raise ValueError (str(key) + " Not Found")
            return self.right.func(key)
        else:
            return self.price


r = Node(1, 6)
r.insert(2, 7)
r.insert(3, 4)
r.insert(4, 7)
r.insert(5, 3)
r.insert(6, 5)
r.insert(7, 8)
r.insert(8, 4)
r.insert(9, 6)
r.insert(10, 4)
try:
    print("Enter key and count:")
    key = int(input())
    count = int(input())
    print(r.func(key) * count)
except ValueError:
    print("Enter int values.")