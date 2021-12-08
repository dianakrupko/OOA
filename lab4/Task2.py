import json

try:
    with open("goods.json", "r") as products:
        dataGoods = json.load(products)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')


class Product:
    """class for Products"""
    def __init__(self, name, quantity_new):
        """
        Initializes all necessary attributes in Composition
        :param name: str, name product
        :param quantity_new:int, the number of products to add
        """
        self.name = name
        self.price = dataGoods[name]["price"]
        self.quantity = dataGoods[name]["quantity"]
        self.quantity_new = quantity_new

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Invalid type of name")
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float) and not isinstance(price, int):
            raise TypeError('Price must be float or int.')
        if price <= 0:
            raise ValueError('Price must be >0')
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be  int.')
        if quantity < 0:
            raise ValueError('Quantity must be >=0')
        self.__quantity = quantity

    @property
    def quantity_new(self):
        return self.__quantity_new

    @quantity_new.setter
    def quantity_new(self, quantity_new):
        if not isinstance(quantity_new, int):
            raise TypeError('Quantity must be  int.')
        if quantity_new < 0:
            raise ValueError('Quantity must be >=0')
        self.__quantity_new = quantity_new

    def __repr__(self):
        self.quantity += self.quantity_new
        return f'\n{self.name}, price: {self.price}, quantity: {self.quantity}'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other


class Composition:
    """class for Composition"""
    def __init__(self):
        self.goods = []

    def __iadd__(self, product):
        if not isinstance(product, Product):
            raise TypeError
        if product in (good.name for good in self.goods):
            self.goods[self.goods.index(product.name)].quantity += product.quantity_new
        else:
            self.goods.append(product)
        return self

    def __isub__(self, product):
        if not isinstance(product, Product):
            raise TypeError
        if product in (good.name for good in self.goods):
            self.goods[self.goods.index(product.name)].quantity -= product.quantity_new
        else:
            self.goods.remove(product)
        return self

    def __mul__(self, other):
        if not isinstance(other, str):
            raise TypeError("Invalid type of product")
        for good in self.goods:
            if good.name == other and good.quantity:
                return f'{other} are available.'
        return f'{other} is not available.'

    def __str__(self):
        return f'{self.goods}'


p1 = Product('hoody', 1)
p2 = Product('jeans', 3)
p3 = Product('sweater', 2)
goods = Composition()
goods += p1
goods += p2
goods -= p2
goods -= p1
goods -= p1
print(goods * "hoody")
print(goods)

