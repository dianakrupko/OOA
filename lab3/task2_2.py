import json
import re
import time
from random import choice

pizza = {
    "Sunday": {
        "name": "\"Paperoni\"",
        "ingredients": [
            "meat",
            "cheese",
            "tomato"
        ],
        "cost": 80
    },
    "Monday": {
        "name": "\"Margarita\"",
        "ingredients": [
            "meat",
            "cheese",
            "sausage"
        ],
        "cost": 70
    },
    "Tuesday": {
        "name": "\"Four Cheeses\"",
        "ingredients": [
            "cheese",
            "tomato",
            "sausage"
        ],
        "cost": 99
    },
    "Wednesday": {
        "name": "\"Calzone\"",
        "ingredients": [
            "cheese",
            "tomato",
            "meat"
        ],
        "cost": 80
    },
    "Thursday": {
        "name": "\"Neapolitan\"",
        "ingredients": [
            "cheese",
            "tomato",
            "beef"

        ],
        "cost": 95
    },
    "Friday": {
        "name": "\"Hunting\"",
        "ingredients": [
            "cheese",
            "tomato",
            "sausage"

        ],
        "cost": 85
    },
    "Saturday": {
        "name": "\"Italian\"",
        "ingredients": [
            "cheese",
            "tomato"
        ],
        "cost": 100
    }
}
with open("pizza.json", "w") as pizzaDay:
    json.dump(pizza, pizzaDay, indent=4)
addingredients = {
    "ketchup": {
        "cost": 25,
        "mass": 10
    },
    "mayonnaise": {
        "cost": 10,
        "mass": 10
    },
    "sauce": {
        "cost": 20,
        "mass": 5
    },
    "season": {
        "cost": 5,
        "mass": 2
    },
    "olive oil": {
        "cost": 18,
        "mass": 50
    }
}

with open("ingred.json", "w") as addIngredients:
    json.dump(addingredients, addIngredients, indent=4)
try:
    with open("pizza.json", "r") as pizzaDay:
        data_pizza = json.load(pizzaDay)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')

try:
    with open("ingred.json", "r") as addIngredients:
        ingredients = json.load(addIngredients)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')


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
        return f"The price of new ingredient {', '.join(self.nameIn)}:{self.sumCostNewIngr()}"


class Sunday(Pizza):
    def __init__(self, day):
        """
        Initializes attributes for the class Pizzeria
        :param day: str, random day
        """
        super().__init__()
        self.day = day
        self.species = data_pizza[day]['name']
        self.pizza_ingredients = data_pizza[day]['ingredients']
        self.costBasePizza = data_pizza[day]['cost']

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not day.isalpha():
            raise ValueError('The day consists of letters')
        self.__day = day

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.costBasePizza
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def __str__(self):
        """
        str method for the class Pizzeria
        :return: string with day, title pizza and pizza ingredient
        """
        return f"Day: {self.day}\nPizza {self.species}:\n\t{', '.join(self.pizza_ingredients)}.\nThe price of PizzaDay {self.species}: {self.sumCostBasePizza()} "


class Monday(Pizza):
    def __init__(self, day):
        """
        Initializes attributes for the class Pizzeria
        :param day: str, random day
        """
        super().__init__()
        self.day = day
        self.species = data_pizza[day]['name']
        self.pizza_ingredients = data_pizza[day]['ingredients']
        self.costBasePizza = data_pizza[day]['cost']

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not day.isalpha():
            raise ValueError('The day consists of letters')
        self.__day = day

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.costBasePizza
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def __str__(self):
        """
        str method for the class Pizzeria
        :return: string with day, title pizza and pizza ingredient
        """
        return f"Day: {self.day}\nPizza {self.species}:\n\t{', '.join(self.pizza_ingredients)}.\nThe price of PizzaDay {self.species}: {self.sumCostBasePizza()} "


class Tuesday(Pizza):
    def __init__(self, day):
        """
        Initializes attributes for the class Pizzeria
        :param day: str, random day
        """
        super().__init__()
        self.day = day
        self.species = data_pizza[day]['name']
        self.pizza_ingredients = data_pizza[day]['ingredients']
        self.costBasePizza = data_pizza[day]['cost']

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not day.isalpha():
            raise ValueError('The day consists of letters')
        self.__day = day

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.costBasePizza
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def __str__(self):
        """
        str method for the class Pizzeria
        :return: string with day, title pizza and pizza ingredient
        """
        return f"Day: {self.day}\nPizza {self.species}:\n\t{', '.join(self.pizza_ingredients)}.\nThe price of PizzaDay {self.species}: {self.sumCostBasePizza()} "


class Wednesday(Pizza):
    def __init__(self, day):
        """
        Initializes attributes for the class Pizzeria
        :param day: str, random day
        """
        super().__init__()
        self.day = day
        self.species = data_pizza[day]['name']
        self.pizza_ingredients = data_pizza[day]['ingredients']
        self.costBasePizza = data_pizza[day]['cost']

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not day.isalpha():
            raise ValueError('The day consists of letters')
        self.__day = day

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.costBasePizza
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def __str__(self):
        """
        str method for the class Pizzeria
        :return: string with day, title pizza and pizza ingredient
        """
        return f"Day: {self.day}\nPizza {self.species}:\n\t{', '.join(self.pizza_ingredients)}.\nThe price of PizzaDay {self.species}: {self.sumCostBasePizza()} "


class Thursday(Pizza):

    def __init__(self, day):
        """
        Initializes attributes for the class Pizzeria
        :param day: str, random day
        """
        super().__init__()
        self.day = day
        self.species = data_pizza[day]['name']
        self.pizza_ingredients = data_pizza[day]['ingredients']
        self.costBasePizza = data_pizza[day]['cost']

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not day.isalpha():
            raise ValueError('The day consists of letters')
        self.__day = day

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.costBasePizza
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def __str__(self):
        """
        str method for the class Pizzeria
        :return: string with day, title pizza and pizza ingredient
        """
        return f"Day: {self.day}\nPizza {self.species}:\n\t{', '.join(self.pizza_ingredients)}.\nThe price of PizzaDay {self.species}: {self.sumCostBasePizza()} "


class Friday(Pizza):
    def __init__(self, day):
        """
        Initializes attributes for the class Pizzeria
        :param day: str, random day
        """
        super().__init__()
        self.day = day
        self.species = data_pizza[day]['name']
        self.pizza_ingredients = data_pizza[day]['ingredients']
        self.costBasePizza = data_pizza[day]['cost']

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not day.isalpha():
            raise ValueError('The day consists of letters')
        self.__day = day

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.costBasePizza
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def __str__(self):
        """
        str method for the class Pizzeria
        :return: string with day, title pizza and pizza ingredient
        """
        return f"Day: {self.day}\nPizza {self.species}:\n\t{', '.join(self.pizza_ingredients)}.\nThe price of PizzaDay {self.species}: {self.sumCostBasePizza()} "


class Saturday(Pizza):
    def __init__(self, day):
        """
        Initializes attributes for the class Pizzeria
        :param day: str, random day
        """
        super().__init__()
        self.day = day
        self.species = data_pizza[day]['name']
        self.pizza_ingredients = data_pizza[day]['ingredients']
        self.costBasePizza = data_pizza[day]['cost']

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not day.isalpha():
            raise ValueError('The day consists of letters')
        self.__day = day

    def sumCostBasePizza(self):
        """
        The method returns the price of the PizzaDay
        :return: string with the name of the pizza and its price
        """
        sumBasePizza = self.costBasePizza
        # return f"The price of PizzaDay {self.species}: {sumBasePizza}"
        return sumBasePizza

    def __str__(self):
        """
        str method for the class Pizzeria
        :return: string with day, title pizza and pizza ingredient
        """
        return f"Day: {self.day}\nPizza {self.species}:\n\t{', '.join(self.pizza_ingredients)}.\nThe price of PizzaDay {self.species}: {self.sumCostBasePizza()} "


class Order():
    def __init__(self, customer, pizzas, n, addingr):
        """
        Itializes all necessary attributes in Order
        :param customer:the customer who places the order
        :param pizzas: pizzas that were ordered
        """
        if not isinstance(addingr, Pizza):
            raise TypeError
        self.customer = customer
        self.pizzas = pizzas
        self.addingr = addingr
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
        total = 0
        total += self.n * self.pizzas.sumCostBasePizza()
        return total + self.addingr.sumCostNewIngr()

    def __str__(self):
        """
        str method for the class Order
        :return: string with customer and the price of his order
        """
        return f"" \
               f"\n\n{'=' * 10}Order{'=' * 10} {self.customer}\n{'-' * 25} \nThe total cost: {self.getTotalCost()}"


today = time.strftime("%A", time.localtime())
#today = choice(list(data_pizza.keys()))
ingr = Pizza(sauce=ingredients["sauce"]["cost"], season=ingredients["season"]["cost"])

def find_day_pizza(self):
    pizza_days = {
        "Sunday": Sunday(today),
        "Monday": Monday(today),
        "Tuesday": Tuesday(today),
        "Wednesday": Wednesday(today),
        'Thursday': Thursday(today),
        "Friday": Friday(today),
        "Saturday": Saturday(today)
    }
    return pizza_days[today]
mypizza=find_day_pizza(today)
print(mypizza)
customer = Customer("Krupko", "Diana", 380971337292)
order = Order(customer, mypizza, 3, ingr)
print(order)
