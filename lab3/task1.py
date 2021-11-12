import json
import numpy as np
from datetime import datetime, date, timedelta
from random import choice, randint, random, randrange

ticketEvent = {
    "Event1": {
        "cost": 220,
        "date":"2021-11-15"
    },
    "Event2": {
        "cost": 150,
        "date":"2022-2-15"
    },
    "Event3": {
        "cost": 190,
        "date":"2021-11-21"
    },
    "Event4": {
        "cost": 250,
        "date":"2021-12-16"
    },
    "Event5": {
        "cost": 270,
        "date":"2021-11-19"
    }
}
with open("ticket.json", "w") as ticketIvent:
    json.dump(ticketEvent, ticketIvent, indent=4)
try:
    with open("pizza.json", "r") as ticketIvent:
        event_titles = json.load(ticketIvent)
except FileNotFoundError:
    raise FileNotFoundError('Error.This file not found')


class Event:
    def __init__(self, title):
        self.title = title
        # self.date = date
        self.regular_price = ticketEvent[title]['cost']
        self.tickets_ordered = 0

    def generate_random_date(self):
        year = np.random.randint(2022, 2025)
        month = np.random.randint(1, 12)
        day = np.random.randint(1, 31)
        return datetime(year, month, day)

    def __str__(self):
        return f"Event: {self.title} \nCost: {self.regular_price}"


class RegularTicket:
    def __init__(self, event):
        self.event = event
        self.regular_price_ticket = ticketEvent[event]['cost']
        self.date=ticketEvent[name_event]["date"]

    def totalcost(self):
        return self.regular_price_ticket

    def identifier(self):
        return id(str(self.event) + str(self.regular_price_ticket)+str(self.totalcost()))

    def __str__(self):
        return f"ID{self.identifier()}\nThe final price: {self.totalcost()}"



class AdvanceTicket(RegularTicket):

    def totalcost(self):
        return (1 - 60 / 100) * self.regular_price_ticket

    def __str__(self):
        return f"ID{self.identifier()}\nThe final price: {self.totalcost()}"


class LateTicket(RegularTicket):
    def totalcost(self):
        return (1 + 10 / 100) * self.regular_price_ticket

    def __str__(self):
        return f"ID{self.identifier()}\nThe final price: {self.totalcost()}"


class StudentTicket(RegularTicket):
    def totalcost(self):
        return 0.5 * self.regular_price_ticket

    def __str__(self):
        return f"ID{self.identifier()}\nThe final price: {self.totalcost()}"


name_event = choice(list(ticketEvent.keys()))
ev = Event(title=name_event)
print(ev)
#dateEvent = ev.generate_random_date().date()

dateEvent=datetime.strptime(ticketEvent[name_event]["date"], "%Y-%m-%d")
dateEv=dateEvent.date()
print("Date of the event: ", dateEv)
datePurchase = datetime.now().date()
#datePurch=datetime.strptime("datePurchase", "%Y-%m-%d")
print("Date of ticket purchase: ", datePurchase)

student = False
day_purchased = dateEv - datePurchase


def ticketSelection():
    if dateEv >= datePurchase:
        if student:
            obj1 = StudentTicket(event=name_event)
            return obj1
        elif day_purchased.days >= 60:
            obj2 = AdvanceTicket(event=name_event)
            return obj2
        elif day_purchased.days <= 10:
            obj3 = LateTicket(event=name_event)
            return obj3
        else:
            obj4 = RegularTicket(event=name_event)
            return obj4
    else:
        return f"The event is over"


myticket = ticketSelection()
print(myticket)

