class Product:

    def __init__(self, name_product, price, dimensions):
        if not isinstance(price, float) and not isinstance(price, int) or not isinstance(dimensions, int):
            raise TypeError('Price must be float or int. Price must be int.')
        if not name_product.isalpha() or price <= 0 or dimensions <= 0:
            raise ValueError('Price and dimensions >0')
        self.name_product = name_product
        self.income = {'price': float(price), 'dimensions': int(dimensions)}

        def showProduct1(self):
            return self.name_product


class AddProduct(Product):
    def __init__(self, name_product, price, dimensions):
        Product.__init__(self, name_product, price, dimensions)

    def showAddProduct(self):
        return self.name_product

    def costAddProduct(self):
        return self.income["price"] * self.income["dimensions"]


class Customer:
    def __init__(self, surname, name, phone):
        if not isinstance(phone, int):
            raise TypeError('The mobile phone must be type int')
        if not surname.isalpha() or not name.isalpha():
            raise ValueError('Incorrect data')
        self.surname = surname
        self.name = name
        self.phone = phone


class Order(Customer, Product):
    def __init__(self, surname, name, phone, name_product, price, dimensions):
        Customer.__init__(self, surname, name, phone)
        Product.__init__(self, name_product, price, dimensions)

    def showCustomer(self):
        return f'\nSurname: {self.surname}\nName: {self.name}\nPhone: {self.phone}'

    def showProduct(self):
        return self.name_product

    def cost(self):
        return self.income["price"] * self.income["dimensions"]


p = Order('Krupko', 'Diana', 380973445648, 'Milk', 8.5, 3)
a = AddProduct('Juice', 6, 8)
print("====Customer====:", p.showCustomer())
print("\nProducts:")
print('--', p.showProduct())
print("Cost:", p.cost())
print('--', a.showAddProduct())
print("Cost:", a.costAddProduct())
print("\nThe total cost:", p.cost() + a.costAddProduct())
