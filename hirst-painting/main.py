from turtle import Screen, Turtle

from colorgram import extract
import random
import turtle

colors = extract('hirst.jpg', 30)
colorList = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colorList.append((r,g,b))

randomColor = colorList[random.choice(colorList)]
timmy = Turtle()

timmy.dot(20, randomColor)



screen = Screen()
screen.exitonclick()


