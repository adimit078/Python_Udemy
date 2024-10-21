import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter color - red, orange, yellow, green, blue, or purple:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


for color in colors:
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(color)
    newTurtle.speed("fastest")
    newTurtle.penup()
    turtles.append(newTurtle)

y = 80
for turtle in turtles:
    turtle.goto(-230,y)
    y-=30

if userBet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if userBet == turtle.pencolor():
                print(f"You won! The winning turtle is {turtle.pencolor()}")
            else:
                print(f"You lost! The winning turtle is {turtle.pencolor()}")

        rDistance = random.randint(0,10)
        turtle.forward(rDistance)

screen.exitonclick()
