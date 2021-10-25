import re


class Product:

    def __init__(self, name_product, price, dimensions):
        """
        Initializes all necessary attributes in Product
        :param name_product: str, name product
        :param price: int, product price
        :param dimensions: float, product dimensions
        """
        self.name_product = name_product
        self.price = price
        self.dimensions = dimensions

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
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, float) and not isinstance(dimensions, int):
            raise TypeError('Dimensions must be float or int.')
        if dimensions <= 0:
            raise ValueError('Dimensions must be >0')
        self.__dimensions = dimensions

    def __str__(self):
        return f'{self.name_product},{self.price},{self.dimensions}'


class Customer:
    def __init__(self, surname, name, phone):
        """
        Initializes all necessary attributes in Customer
        :param surname: str, сustomer surname
        :param name: str, сustomer name
        :param phone: int, phone number customer
        """
        self.surname = surname
        self.name = name
        self.phone = phone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not surname.isalpha():
            raise ValueError('The surname consists of letters')
        self.__surname = surname

    @property
    def name(self):
        return self.__surname

    @name.setter
    def name(self, name):
        if not name.isalpha():
            raise ValueError('The name consists of letters')
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, int):
            raise TypeError('The mobile phone must be type int')
        if not re.match(r"^(\+380|380)\d{9}", str(phone)):
            raise ValueError('Incorrect data.')
        self.__phone =phone

    def __str__(self):
        return f'\nSurname: {self.surname} \nName: {self.name} \nPhone: {self.phone}'


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


Customer_1 = Customer('Krupko', 'Diana', 380973445749)
a = Product('Milk', 7.5, 3)
b = Product('Juice', 10, 2)
c = Product('Bread', 20, 1)
Order_1 = Order(Customer_1, [a])
Order_1.addProduct(b)
Order_1.delProduct(a)
Order_1.addProduct(c)
print(Order_1)
