import json

goods = {"hoody": {"price": 400, "quantity": 10},
         "jeans": {"price": 750, "quantity": 5},
         "sweater": {"price": 600, "quantity": 2}}
with open("goods.json", "w") as products:
    json.dump(goods, products, indent=4)

try:
    with open("goods.json", "r") as products:
        dataGoods = json.load(products)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')


class Composition:

    def __init__(self, name_product):
        """
        Initializes all necessary attributes in Composition
        :param name_product: str, name product
        :param price: float, product price
        :param quantity: int, product quantity
        """
        self.name_product = name_product
        name_pr = dataGoods.keys()
        self.price = dataGoods[name_product]["price"]
        self.quantity = dataGoods[name_product]["quantity"]

    @property
    def name_product(self):
        return self.__name_product

    @name_product.setter
    def name_product(self, name_product):
        if not name_product.isalpha():
            raise ValueError('The name_product consists of letters')
        self.__name_product = name_product

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
            raise ValueError('Guantity must be >=0')
        self.__quantity = quantity

    def changedGoodsPrice(self, name_g, newPr):
        name_goods = name_g
        new_price = newPr
        repWithNewPrice = 'Goods:\n'
        for name_g in dataGoods.keys():
            dataGoods[name_goods]["price"] = new_price
            # self.new_tov = f'{name_g} : {goods[name_g]["price"]}$\n'
        repWithNewPrice += f'{dataGoods}'

        return repWithNewPrice

    def changedGoodsQuantity(self, name_good, newQua):
        name_goods = name_good
        new_Quantity = newQua
        repWithNewQuantity = 'Goods:\n'
        for name_good in dataGoods.keys():
            dataGoods[name_goods]["quantity"] = new_Quantity
        repWithNewQuantity += f'{dataGoods}'

    def __str__(self):
        return f'Product:{self.name_product}\tPrice:{self.price}\tQuantity:{self.quantity}'


a = Composition('hoody')
b = Composition('jeans')

print(a)
print("\n")
print(dataGoods)
print(a.changedGoodsPrice("hoody", 500))
print(b.changedGoodsQuantity("jeans", 8))
with open("goods_new.json", "w") as data:
    json.dump(dataGoods, data, indent=4)
