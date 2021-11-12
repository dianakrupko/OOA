import time
import json
from random import choice
import re

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
        return self.__name

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
        if not re.match(r"^(\+380|380)(\d{9})$", str(phone)):
            raise ValueError('Incorrect data.')
        self.__phone = phone

    def __str__(self):
        """
        str method for the class Customer
        :return: string with surname, name and mobile phone customer
        """
        return f"\nCustomer:\n\tSurname: {self.surname} \n\tName: {self.name} \n\tPhone: {self.phone}"
class Pizza:
    """Superclass Pizza for class Sunday, Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"""

    def __init__(self, **name_ingr):
        """
        Initializes attributes for the class Pizza
        :param name_ingr:dict, all the extra ingredients that are added to the order
        """
        self.name_ingr = name_ingr
        self.nameIn = name_ingr.keys()
        self.costNewIngr = name_ingr.values()
        name_ingr = []

    @property
    def name_ingr(self):
        return self.__name_ingr

    @name_ingr.setter
    def name_ingr(self, name_ingr):
        if not isinstance(name_ingr, dict):
            raise TypeError
        self.__name_ingr = name_ingr

    def sumCostNewIngr(self):
        """
        A method for determining the price of additional ingredients
        :return:price of an additional ingredient
        """
        sumNewIngr = sum(self.costNewIngr)
        return sumNewIngr

    def __str__(self):
        return f"The price of new ingredient {', '.join(self.nameIn)}:{self.sumCostNewIngr()} "


class Sunday(Pizza):

    def __init__(self, name_pizza, price, *base_ingredient, **name_ingr):
        """
        Initializes all necessary attributes in Product
        :param name_pizza: str, name product
        :param price: int, product price
        :param basa_ingredient: float, product dimensions
        """

        super().__init__(**name_ingr)
        self.name_pizza = name_pizza
        self.price = price
        self.base_ingredient = base_ingredient

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.price
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def sumCostNewPizza(self):
        """
        A method for determining the price of pizza with additional ingredients
        :return:price of a new pizza
        """
        sum = self.sumCostBasePizza() + self.sumCostNewIngr()
        return sum

    def __str__(self):
        # return f"{self.name_pizza}\n\t{self.sumCostBasePizza()}{self.base_ingredient}\n***{self.sumCostNewIngr()}"
        return f"Pizza {self.name_pizza}:\n\t{self.base_ingredient}\nThe price of PizzaDay {self.name_pizza}: {self.sumCostBasePizza()} " \
               f"\nThe price of new ingredient {', '.join(self.nameIn)}: {self.sumCostNewIngr()}" \
               f"\nThe price of pizza {self.name_pizza} with new ingredient {', '.join(self.nameIn)}:{self.sumCostNewPizza()}"


class Monday(Pizza):

    def __init__(self, name_pizza, price, *base_ingredient, **name_ingr):
        """
        Initializes all necessary attributes in Product
        :param name_pizza: str, name product
        :param price: int, product price
        :param basa_ingredient: float, product dimensions
        """

        super().__init__(**name_ingr)
        self.name_pizza = name_pizza
        self.price = price
        self.base_ingredient = base_ingredient

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.price
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def sumCostNewPizza(self):
        """
        A method for determining the price of pizza with additional ingredients
        :return:price of a new pizza
        """
        sum = self.sumCostBasePizza() + self.sumCostNewIngr()
        return sum

    def __str__(self):
        # return f"{self.name_pizza}\n\t{self.sumCostBasePizza()}{self.base_ingredient}\n***{self.sumCostNewIngr()}"
        return f"Pizza {self.name_pizza}:\n\t{self.base_ingredient}\nThe price of PizzaDay {self.name_pizza}: {self.sumCostBasePizza()} " \
               f"\nThe price of new ingredient {', '.join(self.nameIn)}: {self.sumCostNewIngr()}" \
               f"\nThe price of pizza {self.name_pizza} with new ingredient {', '.join(self.nameIn)}:{self.sumCostNewPizza()}"


class Tuesday(Pizza):

    def __init__(self, name_pizza, price, *base_ingredient, **name_ingr):
        """
        Initializes all necessary attributes in Product
        :param name_pizza: str, name product
        :param price: int, product price
        :param basa_ingredient: float, product dimensions
        """

        super().__init__(**name_ingr)
        self.name_pizza = name_pizza
        self.price = price
        self.base_ingredient = base_ingredient

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.price
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def sumCostNewPizza(self):
        """
        A method for determining the price of pizza with additional ingredients
        :return:price of a new pizza
        """
        sum = self.sumCostBasePizza() + self.sumCostNewIngr()
        return sum

    def __str__(self):
        # return f"{self.name_pizza}\n\t{self.sumCostBasePizza()}{self.base_ingredient}\n***{self.sumCostNewIngr()}"
        return f"Pizza {self.name_pizza}:\n\t{self.base_ingredient}\nThe price of PizzaDay {self.name_pizza}: {self.sumCostBasePizza()} " \
               f"\nThe price of new ingredient {', '.join(self.nameIn)}: {self.sumCostNewIngr()}" \
               f"\nThe price of pizza {self.name_pizza} with new ingredient {', '.join(self.nameIn)}:{self.sumCostNewPizza()}"


class Wednesday(Pizza):

    def __init__(self, name_pizza, price, *base_ingredient, **name_ingr):
        """
        Initializes all necessary attributes in Product
        :param name_pizza: str, name product
        :param price: int, product price
        :param basa_ingredient: float, product dimensions
        """

        super().__init__(**name_ingr)
        self.name_pizza = name_pizza
        self.price = price
        self.base_ingredient = base_ingredient

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.price
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def sumCostNewPizza(self):
        """
        A method for determining the price of pizza with additional ingredients
        :return:price of a new pizza
        """
        sum = self.sumCostBasePizza() + self.sumCostNewIngr()
        return sum

    def __str__(self):
        # return f"{self.name_pizza}\n\t{self.sumCostBasePizza()}{self.base_ingredient}\n***{self.sumCostNewIngr()}"
        return f"Pizza {self.name_pizza}:\n\t{self.base_ingredient}\nThe price of PizzaDay {self.name_pizza}: {self.sumCostBasePizza()} " \
               f"\nThe price of new ingredient {', '.join(self.nameIn)}: {self.sumCostNewIngr()}" \
               f"\nThe price of pizza {self.name_pizza} with new ingredient {', '.join(self.nameIn)}:{self.sumCostNewPizza()}"


class Thursday(Pizza):

    def __init__(self, name_pizza, price, *base_ingredient, **name_ingr):
        """
        Initializes all necessary attributes in Product
        :param name_pizza: str, name product
        :param price: int, product price
        :param basa_ingredient: float, product dimensions
        """

        super().__init__(**name_ingr)
        self.name_pizza = name_pizza
        self.price = price
        self.base_ingredient = base_ingredient

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.price
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def sumCostNewPizza(self):
        """
        A method for determining the price of pizza with additional ingredients
        :return:price of a new pizza
        """
        sum = self.sumCostBasePizza() + self.sumCostNewIngr()
        return sum

    def __str__(self):
        # return f"{self.name_pizza}\n\t{self.sumCostBasePizza()}{self.base_ingredient}\n***{self.sumCostNewIngr()}"
        return f"Pizza {self.name_pizza}:\n\t{self.base_ingredient}\nThe price of PizzaDay {self.name_pizza}: {self.sumCostBasePizza()} " \
               f"\nThe price of new ingredient {', '.join(self.nameIn)}: {self.sumCostNewIngr()}" \
               f"\nThe price of pizza {self.name_pizza} with new ingredient {', '.join(self.nameIn)}:{self.sumCostNewPizza()}"


class Friday(Pizza):

    def __init__(self, name_pizza, price, *base_ingredient, **name_ingr):
        """
        Initializes all necessary attributes in Product
        :param name_pizza: str, name product
        :param price: int, product price
        :param basa_ingredient: float, product dimensions
        """

        super().__init__(**name_ingr)
        self.name_pizza = name_pizza
        self.price = price
        self.base_ingredient = base_ingredient

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: price
        """
        sumBasePizza = self.price
        return sumBasePizza

    def sumCostNewPizza(self):
        """
        A method for determining the price of pizza with additional ingredients
        :return:price of a new pizza
        """
        sum = self.sumCostBasePizza() + self.sumCostNewIngr()
        return sum

    def __str__(self):
        # return f"{self.name_pizza}\n\t{self.sumCostBasePizza()}{self.base_ingredient}\n***{self.sumCostNewIngr()}"
        return f"Pizza {self.name_pizza}:\n\t{self.base_ingredient}\nThe price of PizzaDay {self.name_pizza}: {self.sumCostBasePizza()} " \
               f"\nThe price of new ingredient {', '.join(self.nameIn)}: {self.sumCostNewIngr()}" \
               f"\nThe price of pizza {self.name_pizza} with new ingredient {', '.join(self.nameIn)}:{self.sumCostNewPizza()}"


class Saturday(Pizza):

    def __init__(self, name_pizza, price, *base_ingredient, **name_ingr):
        """
        Initializes all necessary attributes in Product
        :param name_pizza: str, name product
        :param price: int, product price
        :param basa_ingredient: float, product dimensions
        """

        super().__init__(**name_ingr)
        self.name_pizza = name_pizza
        self.price = price
        self.base_ingredient = base_ingredient

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.price
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def sumCostNewPizza(self):
        """
        A method for determining the price of pizza with additional ingredients
        :return:price of a new pizza
        """
        sum = self.sumCostBasePizza() + self.sumCostNewIngr()
        return sum

    def __str__(self):
        # return f"{self.name_pizza}\n\t{self.sumCostBasePizza()}{self.base_ingredient}\n***{self.sumCostNewIngr()}"
        return f"Pizza {self.name_pizza}:\n\t{self.base_ingredient}\nThe price of PizzaDay {self.name_pizza}: {self.sumCostBasePizza()} " \
               f"\nThe price of new ingredient {', '.join(self.nameIn)}: {self.sumCostNewIngr()}" \
               f"\nThe price of pizza {self.name_pizza} with new ingredient {', '.join(self.nameIn)}:{self.sumCostNewPizza()}"

class Order():
    def __init__(self, customer, pizzas, n):
        """
        Itializes all necessary attributes in Order
        :param customer:the customer who places the order
        :param pizzas: pizzas that were ordered
        """

        self.customer = customer
        self.pizzas = pizzas
        self.n = n

        @property
        def customer(self):
            return self.__customer

        @customer.setter
        def customer(self, customer):
            if not isinstance(customer, Customer):
                raise TypeError
            self.__customer = customer

    def getTotalCost(self):
        """
        The method returns the price of the entire order
        :return: total cost
        """
        total=0
        total += self.n*self.pizzas
        return total

    def __str__(self):
        """
        str method for the class Order
        :return: string with customer and the price of his order
        """
        return f"" \
               f"\n\n{'=' * 10}Order{'=' * 10} {self.customer}\n{'-' * 25} \nThe total cost: {self.getTotalCost()}"


today = time.strftime("%A", time.localtime())
sundayPizza = Sunday("\"Paperoni\"", 100, "onion", "meat", "cheese", tomato=20)
mondayPizza = Monday("\"Margarita\"", 80, "meat", "beef", potato=15)
tuesdayPizza = Tuesday("\"Four Cheeses\"", 105, "onion", "meat", "beef", potato=15)
wednesdayPizza = Wednesday("\"Neopolitan\"", 96, "onion", "meat", "beef", chicken=30)
thursdayPizza = Thursday("\"Calzone\"", 99, "onion", "meat", "beef", cheese=30)
fridayPizza = Friday("\"Hunting\"", 90, "cheese","meat", "beef", chicken=30, potato=15)
saturdayPizzza = Saturday("\"Neopolitano\"", 87, "meat", "beef", chicken=30, onion=5)

obj = {
    "Sunday": sundayPizza.__str__(),
    "Monday": mondayPizza.__str__(),
    "Tuesday": tuesdayPizza.__str__(),
    "Wednesday": wednesdayPizza.__str__(),
    "Thursday": thursdayPizza.__str__(),
    "Friday": fridayPizza.__str__(),
    "Saturday": sundayPizza.__str__()

}

with open("obPizza.json", "w") as pizzaDays:
    json.dump(obj, pizzaDays, indent=4)
costPizza={
    "Sunday": 120,
    "Monday": 95,
    "Tuesday": 120,
    "Wednesday": 126,
    "Thursday": 129,
    "Friday": 135,
    "Saturday": 120
}
with open("PizzaCost.json", "w") as pizzaCost:
    json.dump(costPizza, pizzaCost, indent=4)
try:
    with open("obPizza.json", "r") as pizzaDay:
        pizzaDaysWeek = json.load(pizzaDay)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')

try:
    with open("PizzaCost.json", "r") as pizzaCost:
        pizzaDayCost = json.load(pizzaCost)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')


def pizzaDaySelection(day):
    if day == "Sunday":
        return pizzaDaysWeek["Sunday"]
    elif day == "Monday":
        return pizzaDaysWeek["Monday"]
    elif day == "Tuesday":
        return pizzaDaysWeek["Tuesday"]
    elif day == "Wednesday":
        return pizzaDaysWeek["Wednesday"]
    elif day == "Thursday":
        return pizzaDaysWeek["Thursday"]
    elif day == "Friday":
        return pizzaDaysWeek["Friday"]
    elif day == "Saturday":
        return pizzaDaysWeek["Saturday"]
    else:
        return f"Error"

def pizzaCostSelection(day):
    if day == "Sunday":
        return pizzaDayCost["Sunday"]
    elif day == "Monday":
        return pizzaDayCost["Monday"]
    elif day == "Tuesday":
        return pizzaDayCost["Tuesday"]
    elif day == "Wednesday":
        return pizzaDayCost["Wednesday"]
    elif day == "Thursday":
        return pizzaDayCost["Thursday"]
    elif day == "Friday":
        return pizzaDayCost["Friday"]
    elif day == "Saturday":
        return pizzaDayCost["Saturday"]
    else:
        return f"Error"
mypizza = pizzaDaySelection(today)
print(mypizza)
mypizza1 = pizzaCostSelection(today)

customer = Customer("Krupko", "Diana", 380971337292)
order = Order(customer, mypizza1, 3)
print(order)