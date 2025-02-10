import random
from turtle import Turtle

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Creates a new car
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(310, random_y)
            self.all_cars.append(car)

    # Moves the cars along the X axis
    def move_cars(self):
        for car in self.all_cars:
            # Deletes the car when it goes out of screen
            if car.xcor() < -320:
                car.clear()
                del car
                continue
            car.backward(self.car_speed)

    # Increases the speed of cars
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
