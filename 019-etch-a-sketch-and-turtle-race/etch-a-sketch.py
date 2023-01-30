import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
screen.listen()

def move_forwards():
    tim.forward(10)

def move_back():
    tim.back(10)

def rotate_clockwise():
    tim.right(10)

def rotate_counterclockwise():
    tim.left(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_forwards, "w")
screen.onkey(move_back, "s")
screen.onkey(rotate_clockwise, "d")
screen.onkey(rotate_counterclockwise, "a")
screen.onkey(clear_drawing, "c")

screen.exitonclick()