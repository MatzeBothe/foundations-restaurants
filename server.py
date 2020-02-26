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

def show_restaurants(all_restaurants):
    for line in all_restaurants:
        line = line[4:]
        name = line.split(",")[0]
        location = line.split(",")[1]
        restaurant = Restaurant(name, location)
        tm = Template("The name is {{ per.getName() }} and it is located in {{ per.getLocation() }}")
        msg = tm.render(per=restaurant)
        print(msg)

data.close()