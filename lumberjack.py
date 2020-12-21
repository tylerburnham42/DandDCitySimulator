from person import Person
from resource import Resource
import random

FIRST_NAME = ["Fir", "Maple", "Dogwood", "Pecan", "Oak"]
LAST_NAME = ["Jenkins", "Bill", "Woodson", "Strong-hand", "Dan", "Bob"]

FACTOR = 1

class Lumberjack(Person):

    def __init__(self, skill, money):
        self.name = "{} {}".format(random.choice(FIRST_NAME), random.choice(LAST_NAME))
        self.profession = "Lumberjack"
        self.skill = skill
        self.money = money


    def make(self, resources, time):
        produced = []
        for resource in resources:
            if resource.name == "Tree":

                quantity_in = resource.quantity - self.skill
                quantity_in = quantity_in if quantity_in else resource.quantity

                money = resource.value

                quantity = quantity_in * resource.quality
                quality = 5
                value = resource.value + quality * FACTOR
                lumber = Resource("Wood", quantity, self, quality, value, time)
                produced.append(lumber)


        return produced