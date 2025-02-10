from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("classic")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.exitonclick()
