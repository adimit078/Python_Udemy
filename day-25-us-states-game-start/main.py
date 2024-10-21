import turtle
from turtle import Turtle

import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


gameDone = False
df = pd.read_csv("50_states.csv")

guessed_states = []
states = df["state"].to_list()
while len(guessed_states) < 50:
    state_input = screen.textinput(title = f"{len(guessed_states)}/50 Guessed Correctly", prompt = "What's another state's name?")
    if state_input == "Exit":
        missing_states = [state for state in states if (state not in guessed_states)]
        missing_states_data = pd.dataFrame(missing_states)
        missing_states_data.to_csv("missing_states")
    if state_input in states:
        guessed_states.append(state_input)

        state_value = df[df["state"] == state_input]
        x, y = state_value["x"].values[0], state_value["y"].values[0]
        stateTurtle = Turtle()
        stateTurtle.hideturtle()
        stateTurtle.penup()
        stateTurtle.goto(x,y)
        stateTurtle.write(state_input)

with open("missedStates.txt", "a") as file:
    for state in states:
        if state not in guessed_states:
            file.write(f"{state}\n")