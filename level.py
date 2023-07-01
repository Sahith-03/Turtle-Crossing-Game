from turtle import Turtle

class Level(Turtle):

    def __init__(self):
        self.lev = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.display()

    def inc_level(self):
        self.lev += 1
        self.display()

    def display(self):
        self.clear()
        self.goto(-235,255)
        self.write(f"Level: {self.lev}", move=False, align="center", font=("Times New Roman",24,"normal"))

    def exit(self):
        self.goto(0,0)
        self.write(f"Game Over",move=True,align="center",font=("Times New Roman",50,"normal"))