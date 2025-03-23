COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(x=(random.randint(280,300)), y=(random.randint(-250,250)))

    def move_car(self):
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)

