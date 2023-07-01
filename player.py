from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(0, -280)

    def go_up(self):
        self.forward(10)

    def restart(self):
        self.goto(0,-280)