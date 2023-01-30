import turtle
import random

tim = turtle.Turtle()
tim.speed("fastest")
turtle.colormode(255)

# colour_list comes from the extracted data from the colour-extraction.py file: -
colour_list = [(202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72), (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101), (176, 192, 209)]

tim.hideturtle()
tim.penup()
tim.back(225)
tim.setheading(270)
tim.forward(225)
tim.setheading(0)

for i in range(10):
    for i in range(10):
        tim.dot(20, random.choice(colour_list))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    tim.back(500)

screen = turtle.Screen()
screen.exitonclick()