import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Makes the screen object and modifies it
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Makes objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Takes user key presses to move paddles
screen.listen()
screen.onkeypress(player.move, "w")


# Main While Loop
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detects collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    # Detects if player has crossed the line
    if player.ycor() > 290:
        player.goto(x=0, y=-280)  # goes back to the starting position
        car_manager.level_up()
        scoreboard.increase_level()


# Exits the program with mouse click
screen.exitonclick()
