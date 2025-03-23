import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()

cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    random_chance = random.randint(1,6)
    if random_chance ==1:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.move_car()
        if player.distance(car) < 20:
            scoreboard.game_over()
            player.goto(0, -280)
            game_is_on = False

    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.point()
    # print(player.pos())








