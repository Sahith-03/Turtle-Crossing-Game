from turtle import Turtle
import random
colors = ["red","orange","blue","yellow","green","purple"]

class car_manager():

    def __init__(self):
        self.all_cars = []
        self.dis = 5
    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            y = random.randint(-220,220)
            new_car.goto(300,y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.dis)

    def inc_speed(self):
        self.dis += 2