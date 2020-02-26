#!/usr/bin/env python3

path = "/Users/matthias.bothe/code/foundations/foundations-restaurants/restaurants.txt"
data = open(path, "r")
content = data.read()

def generate_html(content):
    print("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Success!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/style.css">
  </head>  
  <body style="text-align:left">
    <h1>Restaurant list</h1>
    <p>{}</p>
  </body>
</html>
""".format(content)
    )

data.close()