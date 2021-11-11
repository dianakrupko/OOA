import json
import re
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

addingredients = {
    "chicken": {
        "cost": 25,
        "mass": 100
    },
    "potato": {
        "cost": 10,
        "mass": 100
    },
    "beef": {
        "cost": 20,
        "mass": 100
    },
    "onion": {
        "cost": 5,
        "mass": 100
    },
    "mushroom": {
        "cost": 18,
        "mass": 100
    }
}

with open("pizza.json", "w") as pizzaDay:
    json.dump(pizza, pizzaDay, indent=4)

with open("pizza.json", "r") as pizzaDay:
    data_pizza = json.load(pizzaDay)

with open("addIngredients.json", "w") as addIngredients:
    json.dump(addingredients, addIngredients, indent=4)

with open("addIngredients.json", "r") as addIngredients:
    ingredients = json.load(addIngredients)


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


class Pizzeria:
    """Superclass for class Pizza"""

    def __init__(self, day):
        """
        Initializes attributes for the class Pizzeria
        :param day: str, random day
        """
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


class Pizza(Pizzeria):
    """Subslass of the class Pizzeria"""

    def __init__(self, **name_ingr):
        """
        Initializes attributes for the class Pizza
        :param name_ingr:dict, all the extra ingredients that are added to the pizza
        """
        super().__init__(day=random_day)
        self.name_ingr = name_ingr
        self.nameIn = name_ingr.keys()
        self.costNewIngr = name_ingr.values()
        name_ingr = []

    @property
    def name_ingr(self):
        return self.__name_ingr

    @name_ingr.setter
    def name_ingr(self,name_ingr):
        if not isinstance(name_ingr, dict):
            raise TypeError
        self.__name_ingr = name_ingr

    def sumCostNewIngr(self):
        """
        A method for determining the price of additional ingredients
        :return:price of an additional ingredient
        """
        sumNewIngr = sum(self.costNewIngr)
        # return f"The price of an additional ingredient: {sumNewIngr}"
        return sumNewIngr

    def sumCostNewPizza(self):
        """
        A method for determining the price of pizza with additional ingredients
        :return:price of a new pizza
        """
        sum = self.sumCostBasePizza() + self.sumCostNewIngr()
        return sum

    def returnNewPizza(self):
        return f"The price of new ingredient {', '.join(self.nameIn)}: {self.sumCostNewIngr()}" \
               f"\nThe price of pizza with the following ingredients: {', '.join(self.pizza_ingredients)}, {', '.join(self.nameIn)}:{self.sumCostNewPizza()}"


class Order():
    def __init__(self, customer, pizzas):
        """
        Itializes all necessary attributes in Order
        :param customer:the customer who places the order
        :param pizzas: pizzas that were ordered
        """
        if not all([isinstance(pizz, Pizza) for pizz in pizzas]):
            raise TypeError("Wrong type")
        if not isinstance(customer, Customer):
            raise TypeError
        self.customer = customer
        self.pizzas = pizzas

    def addPizza(self, new_pizza):
        """
        The method adds pizza to order
        :param new_pizza: new pizza with or without additional ingredients
        """
        if not isinstance(new_pizza, Pizza):
            raise TypeError
        self.pizzas.append(new_pizza)

    def delPizza(self, name_pizza):
        """
        The method that removes pizza from the order
        :param name_pizza: the name of the pizza to be removed from the order
        """
        if not isinstance(name_pizza, Pizza):
            raise TypeError
        self.pizzas.remove(name_pizza)

    def getTotalCost(self):
        """
        The method returns the price of the entire order
        :return: total cost
        """
        total = 0
        for pizz in self.pizzas:
            total += pizz.sumCostNewPizza()
        return total

    def __str__(self):
        """
        str method for the class Order
        :return: string with customer and the price of his order
        """
        return f"{'=' * 10}Order{'=' * 10} {self.customer}\n{'-' * 25} \nThe total cost: {self.getTotalCost()}"


random_day = choice(list(data_pizza.keys()))

customer = Customer("Krupko", "Diana", 380971337292)

pizza1 = Pizza(beef=ingredients["beef"]["cost"], potato=ingredients["potato"]["cost"])
#pizza1=Pizza(["potato","beef"])
print(pizza1)
print(pizza1.returnNewPizza())

pizza2 = Pizza(mushroom=ingredients["mushroom"]["cost"])
print(pizza2.returnNewPizza())

pizza3 = Pizza(chicken=ingredients["chicken"]["cost"])
print(pizza3.returnNewPizza())

order = Order(customer, [pizza1, pizza2])
print(order)

order.addPizza(pizza3)
print("With add pizza: ", order.getTotalCost())

order.delPizza(pizza1)
print("After removing the pizza: ", order.getTotalCost())
