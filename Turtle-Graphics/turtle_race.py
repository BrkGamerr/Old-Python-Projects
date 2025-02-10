import random
from turtle import Turtle, Screen

# Makes the screen and sets it's dimensions.
screen = Screen()
screen.setup(width=800, height=700)

# Different variables.
colors = ["red", "orange", "green", "blue", "purple"]
y_positions = [-60, -30, 0, 30, 60,]
all_turtles = []
race_on = True


# Adds turtles to race.
def add_turtles(number: int):
    for _ in range(number):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[_])
        new_turtle.penup()
        new_turtle.goto(x=-390, y=y_positions[_])
        all_turtles.append(new_turtle)


# Randomly moves the turtles forward.
def turtle_move():
    random_distance = random.randint(0, 10)
    turtle.forward(random_distance)


# Ends the race.
def end_race():
    global race_on
    race_on = False
    winning_color = turtle.pencolor()  # Gets the color of turtle who won.
    # Checks if the user has guessed the winner.
    if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
    else:
        print(f"You've lost! The {winning_color} turtle is the winner!")


# Asks the user to choose the number of turtles to race.
add_turtles(int(screen.textinput(title="Number of Turtles", prompt="How many turtles would you like: ").lower()))

# Asks the user to choose the winning color.
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win: ").lower()


# Main Code
while race_on:
    # Loops through all the turtles and move them forward.
    for turtle in all_turtles:
        # When a turtle hits the "wall" end the race.
        if turtle.xcor() > 370:
            end_race()

        turtle_move()


# Exit the screen with mouse click.
screen.exitonclick()
