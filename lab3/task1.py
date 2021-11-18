import json
import numpy as np
import re
from datetime import datetime, date, timedelta
from random import choice, randint, random, randrange
from task1_const import ADVANCE, LATE, STUDENT

ticketEvent = {
    "Popular IT cases": {
        "cost": 220,
        "date": "2021-12-13"
    },
    "Vodafone Data Science": {
        "cost": 150,
        "date": "2022-2-15"
    },
    "Data Sciense Competition": {
        "cost": 200,
        "date": "2021-11-22"
    },
    "Soft skills for IT": {
        "cost": 250,
        "date": "2021-12-16"
    },
    "How to start a career in IT": {
        "cost": 270,
        "date": "2021-11-19"
    }
}
with open("ticket.json", "w") as ticketIvent:
    json.dump(ticketEvent, ticketIvent, indent=4)
try:
    with open("ticket.json", "r") as ticketIvent:
        event_titles = json.load(ticketIvent)
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


class Event:
    """Class Event"""
    def __init__(self, title):
        """
        Initializes attributes for the class Event
        :param title: str, name event
        """
        self.title = title
        self.regular_price = event_titles[title]['cost']

        @property
        def title(self):
            return self.__title

        @title.setter
        def title(self, title):
            if not isinstance(title, str):
                raise TypeError('The title consists of letters')
            if title not in event_titles.keys():
                raise ValueError("There is no such event")
            self.__title = title

    def generate_random_date(self):
        year = np.random.randint(2021, 2025)
        month = np.random.randint(1, 12)
        day = np.random.randint(1, 31)
        return datetime(year, month, day)

    def __str__(self):
        return f"Event: {self.title} \nCost: {self.regular_price}"


class RegularTicket:
    """Superclass for class RegularTicket"""
    def __init__(self, event):
        """
        Initializes attributes for the class RegularTicket
        :param event: str,name event
        """
        self.event = event
        self.regular_price_ticket = event_titles[event]['cost']
        self.dateEv = datetime.strptime(event_titles[name_event]["date"], "%Y-%m-%d")
        self.date = self.dateEv.date()
        self.id = self.identifier()

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event):
        if not isinstance(event, str):
            raise TypeError('The event consists of letters')
        if event not in event_titles.keys():
            raise ValueError("There is no such event")
        self.__event = event

    def totalcost(self):
        return self.regular_price_ticket

    def identifier(self):
        return  id(str(self.event) + str(self.regular_price_ticket) + str(self.date))

    def __str__(self):
        return f"ID{self.id}\nThe final price: {self.totalcost()}"


class AdvanceTicket(RegularTicket):
    """Subslass of the class RegularTicket"""
    def totalcost(self):
        return ADVANCE * self.regular_price_ticket


class LateTicket(RegularTicket):
    """Subslass of the class RegularTicket"""
    def totalcost(self):
        return LATE * self.regular_price_ticket



class StudentTicket(RegularTicket):
    """Subslass of the class RegularTicket"""
    def totalcost(self):
        return STUDENT * self.regular_price_ticket

    # def __str__(self):
    #    return f"ID{self.identifier()}\nThe final price: {self.totalcost()}"


class Order():
    def __init__(self, customer, tickets):
        """
        Itializes all necessary attributes in Order
        :param customer:the customer who places the order
        :param tickets: tickets that were ordered
        """
        if not all([isinstance(tick, RegularTicket) or isinstance(tick, AdvanceTicket) or isinstance(tick,LateTicket) or isinstance( tick, StudentTicket) for tick in tickets]):
            raise TypeError("Wrong type")
        if not isinstance(customer, Customer):
            raise TypeError("Wrong type")
        self.customer = customer
        self.tickets = tickets

    def addTicket(self, new_ticket):
        """
        The method adds tickets
        :param new_ticket: new ticket
        """
        if not isinstance(new_ticket, RegularTicket) and not isinstance(new_ticket, AdvanceTicket) and not isinstance(
                new_ticket, LateTicket) and not isinstance(new_ticket, StudentTicket):
            raise TypeError
        self.tickets.append(new_ticket)

    def delTicket(self, name_ticket):
        """
        The method that removes ticket
        :param name_ticket: the name of the ticket to be removed from the order
        """
        if not isinstance(name_ticket, RegularTicket) and not isinstance(name_ticket, AdvanceTicket) and not isinstance(
                name_ticket, LateTicket) and not isinstance(name_ticket, StudentTicket):
            raise TypeError
        self.tickets.remove(name_ticket)

    def getTotalCost(self):
        """
        The method returns the price of the entire order
        :return: total cost
        """
        total = 0
        for tick in self.tickets:
            total += tick.totalcost()
        return total

    def __str__(self):
        """
        str method for the class Order
        :return: string with customer and the price of his order
        """
        return f"{'=' * 10}MyTickets{'=' * 10} {self.customer}\n{'-' * 25}\nThe total cost: {self.getTotalCost()}"


name_event = choice(list(event_titles.keys()))
# datePurch = datetime.now()


def ticketSelection(name_eve):
    ev = Event(title=name_eve)
    print(ev)
    dateEvent = datetime.strptime(event_titles[name_eve]["date"], "%Y-%m-%d")
    dateEv = dateEvent.date()
    print("Date of the event: ", dateEv)

    datePurch = datetime.now()
    datePurchase = datePurch.date()
    print("Date of ticket purchase: ", datePurchase)

    student = False
    day_purchased = dateEv - datePurchase

    if dateEv >= datePurchase:
        if student:
            obj1 = StudentTicket(event=name_eve)
            return obj1
        elif day_purchased.days >= 60:
            obj2 = AdvanceTicket(event=name_eve)
            return obj2
        elif day_purchased.days <= 10:
            obj3 = LateTicket(event=name_eve)
            return obj3
        else:
            obj4 = RegularTicket(event=name_eve)
            return obj4
    else:
        return f"The event is over"


myticket1 = ticketSelection(choice(list(event_titles.keys())))
print(myticket1)
print('-' * 20)
myticket2 = ticketSelection(choice(list(event_titles.keys())))
print(myticket2)
# print('-' * 20)
# myticket3 = ticketSelection(choice(list(event_titles.keys())))
# print(myticket3)

customer = Customer("Krupko", "Diana", 380971337292)
od = Order(customer, [myticket1, myticket2])
print("\n")
print(od)
# od.addTicket(myticket3)
# print(od)
# od.delTicket(myticket3)
# print(od)
