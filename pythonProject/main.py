import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.setup(startx=350,starty=0)

def up():
    paddle.setpos(paddle.xcor(), paddle.ycor() + 20)

def down():
    paddle.setpos(paddle.xcor(), paddle.ycor() - 20)


screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")

screen.exitonclick()




