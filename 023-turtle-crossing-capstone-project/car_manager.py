import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setx(300)
            new_car.sety(random.randint(-250, 250))
            self.cars.append(new_car)
    
    def car_move(self):
        for car in self.cars:
            car.back(self.car_speed)
    
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

