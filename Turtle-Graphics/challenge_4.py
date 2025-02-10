import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("classic")
tim.pensize(10)
tim.speed("fast")

screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_direction():
    direction = random.choice(directions)
    return direction


for _ in range(50):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random_direction())

screen.exitonclick()
