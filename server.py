#!/usr/bin/env python3
from jinja2 import Template

path = "/Users/matthias.bothe/code/foundations/foundations-restaurants/restaurants.txt"
data = open(path, "r")
all_restaurants = data.read()

class Restaurant:

    def __init__(self, name, location):

        self.name = name
        self.location = location

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

for restaurant in all_restaurants:
    restaurant = Restaurant()

    tm = Template("The name is {{ per.getName() }} and it is located in {{ per.getLocation() }}")
    msg = tm.render(per=restaurant)
    print(msg)

data.close()