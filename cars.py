from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "orange", "purple"]
INITIAL_SPEED = 5
BOOST_SPEED = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.initial_speed = INITIAL_SPEED

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_car(self):
        for i in self.all_cars:
            i.backward(self.initial_speed)

    def speed_up(self):
        self.initial_speed += BOOST_SPEED
