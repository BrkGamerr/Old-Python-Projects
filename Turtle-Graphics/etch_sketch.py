from turtle import Turtle, Screen

# making objects from Classes
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_drawing():
    screen.reset()


# set focus on TurtleScreen (in order to collect key-events)
screen.listen()

# assigning keys to trigger a function
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=turn_left, key="d")
screen.onkeypress(fun=turn_right, key="a")
screen.onkeypress(fun=clear_drawing, key="c")

screen.exitonclick()
