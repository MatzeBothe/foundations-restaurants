#!/usr/bin/env python3
from jinja2 import Template
import cgi

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
        print ("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
  </head>  
  <body>
    <h1>{}.</h1>
    <a href="/index.html">Try again</a>
  </body>
</html>
""".format(msg)
        )

data.close()