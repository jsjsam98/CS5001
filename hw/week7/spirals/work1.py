from turtle import *
import random
setheading(90)
total_color = ['red2', 'dark orange', 'yellow2',
               'green2', 'cyan2', 'blue', 'purple3']
pensize(6)
colormode(255)
bgcolor('black')
speed(0)
length = 50
tracer(0)
for j in range(0, 7):
    length += 30
    pensize(6+j)
    for i in range(0, 20):

        penup()
        color_circle = total_color[j]
        forward(length)
        left(90)
        pendown()
        pencolor(color_circle)
        forward(length)
        left(90)
        forward(length)
        left(90)
        penup()
        forward(length)
        left(90)

        left(18)
        penup()

hideturtle()

ts = getscreen()
ts.getcanvas().postscript(file="work1.eps")
done()
