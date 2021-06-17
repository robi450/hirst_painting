import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()

color_list = [(38, 93, 151), (184, 41, 78), (179, 165, 32), (227, 208, 88), (213, 153, 86), (113, 178, 209), (215, 231, 223), (131, 87, 61), (229, 69, 51), (203, 76, 129), (218, 129, 178), (83, 109, 201), (22, 168, 116), (49, 136, 95), (108, 205, 194), (107, 48, 37), (52, 58, 95), (139, 36, 82), (27, 174, 192), (216, 204, 36), (220, 173, 190), (178, 186, 213), (225, 174, 167), (157, 206, 221), (153, 210, 200), (39, 83, 85), (40, 83, 82)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

