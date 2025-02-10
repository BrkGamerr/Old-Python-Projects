import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("classic")
tim.speed("fastest")

screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.right(size_of_gap)


draw_spirograph(15)

screen.exitonclick()
