from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("classic")


def triangle():
    tim.color("DarkRed")
    for _ in range(3):
        tim.forward(100)
        tim.right(120)


def square():
    tim.color("green")
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def pentagon():
    tim.color("DarkGoldenrod")
    for _ in range(5):
        tim.forward(100)
        tim.right(72)


def hexagon():
    tim.color("DeepPink")
    for _ in range(6):
        tim.forward(100)
        tim.right(60)


def heptagon():
    tim.color("chocolate")
    for _ in range(7):
        tim.forward(100)
        tim.right(51.42)


def octagon():
    tim.color("DeepSkyBlue")
    for _ in range(8):
        tim.forward(100)
        tim.right(45)


def nonagon():
    tim.color("navy")
    for _ in range(9):
        tim.forward(100)
        tim.right(40)


def decagon():
    tim.color("SlateGray")
    for _ in range(10):
        tim.forward(100)
        tim.right(36)


def draw():
    triangle()
    square()
    pentagon()
    hexagon()
    heptagon()
    octagon()
    nonagon()
    decagon()


draw()

screen.exitonclick()
