import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Choose the color of the turtle you bet on: ")
colors = ["red", "orange", "yellow", "green" , "blue", "purple"]
all_turtles = []

y_axis=-180
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    y_axis +=50
    new_turtle.goto(-230, y_axis)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have won! The {winner} turtle is the winner!")
            else:
                print(f"You have lost! The {winner} turtle is the winner!")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()