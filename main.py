from turtle import Turtle, Screen
from player import Player
from level import Level
from cars import car_manager
import time

screen = Screen()
screen.setup(600,600)
screen.tracer(0)

level = Level()
car = car_manager()
player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    # Next Level
    if player.ycor()>=290:
        car.inc_speed()
        level.inc_level()
        player.restart()
    # Collide with a car(GAME OVER)
    for obstacle in car.all_cars:
        if obstacle .distance(player)<20:
            game_is_on = False
            level.exit()
            break
screen.exitonclick()