import turtle as t
import random
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(2)
timmy.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def draw_spire(size):
# 3. Draw Stirograph
    degrees = 360
    for _ in range(int(360 / size)):
        timmy.circle(50)
        timmy.color(random_color())
        degrees -= size
        timmy.penup()
        timmy.setheading(degrees)
        timmy.forward(10)
        timmy.pendown()
        timmy.circle(50)

draw_spire(5)





screen = t.Screen()
screen.exitonclick()

# # 1. draw shapes with diff number of sides
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#
#          timmy.forward(100)
#          timmy.right(angle)
#
# for shape_side_n in  range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)
#



# 2.  Draw random road
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r,g,b)
#
#
# directions = [0,90,180,270]
#
# def draw_road():
#     for _ in range(100):
#          timmy.forward(30)
#          timmy.color(random_color())
#          timmy.setheading(random.choice(directions))
#
#
#
# draw_road()