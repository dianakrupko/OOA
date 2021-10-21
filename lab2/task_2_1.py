import re


class Product:

    def __init__(self, name_product, price, dimensions):
        if not isinstance(price, float) and not isinstance(price, int) or not isinstance(dimensions, int):
            raise TypeError('Price must be float or int.')
        if not isinstance(dimensions, int):
            raise TypeError(' Dimensions must be int.')
        if not name_product.isalpha():
            raise ValueError('The name consists of letters')
        if price <= 0:
            raise ValueError('Price must be >0')
        if dimensions <= 0:
            raise ValueError('Dimensions must be >0')
        self.name_product = name_product
        self.price = price
        self.dimensions = dimensions

    def __str__(self):
        pass


class Customer:
    def __init__(self, surname, name, phone):
        if not isinstance(phone, int):
            raise TypeError('The mobile phone must be type int')
        if not re.match(r'^[+380]\d*', str(phone)) or len(str(phone)) != 12:
            raise ValueError('Incorrect data.Phone number +380_________')
        if not surname.isalpha() or not name.isalpha():
            raise ValueError('Incorrect data')
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'\nSurname: {self.surname} \nName: {self.name} \nPhone: +{self.phone}'


class Order:
    def __init__(self, customer, products):
        if not all([isinstance(product, Product) for product in products]):
            raise TypeError("Wrong type")
        if not isinstance(customer, Customer):
            raise TypeError
        self.customer = customer
        self.products = products

    def addProduct(self, new_prod):
        if not isinstance(new_prod, Product):
            raise TypeError
        self.products.append(new_prod)

    def delProduct(self, name_product):
        if not isinstance(name_product, Product):
            raise TypeError
        self.products.remove(name_product)

    def getTotalCost(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def __str__(self):
        return f'=====Customer===== {self.customer}\nThe total cost:: {self.getTotalCost()}'


Customer_1 = Customer('Krupko', 'Diana', +380973445648)
a = Product('Milk', 7.5, 3)
b = Product('Juice', 10, 2)
c = Product('Bread', 20, 1)
Order_1 = Order(Customer_1, [a])
Order_1.addProduct(b)
Order_1.delProduct(a)
Order_1.addProduct(c)
print(Order_1)
