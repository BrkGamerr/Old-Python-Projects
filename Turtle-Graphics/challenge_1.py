from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

tim.shape("classic")


def square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


square()

screen.exitonclick()
