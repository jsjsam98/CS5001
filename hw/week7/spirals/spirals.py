'''
Shangjun Jiang
CS 5001, Fall 2020
HW 6 -- spiral

This is a rotated snake program
Please run the program and see what happens
'''
from turtle import *
from math import *
import random


def ring(r):
    speed(0)
    colormode(255)
    bgcolor('white')
    pi = 3.1415926
    tracer(0)
    r_outer = 1.15*r
    step1 = 2*pi*r/360
    step2 = 2*pi*r_outer/360

    d = r_outer-r
    # calculate the denominator
    sum_vertical = 0
    for i in range(30):
        sum_vertical += i*sin(i*3/180*pi)
    sum_vertical = sum_vertical*2
    step_oval = d/sum_vertical
    penup()
    pencolor('white')
    pensize(0.1)
    # draw inner circle
    pendown()
    for i in range(0, 360):
        forward(step1)
        rt(1)
    pensize(1)
    penup()
    # draw little gray circle
    count = 0
    for i in range(0, 360):
        forward(step1)
        rt(1)
        if count % 18 == 0:
            pendown()
            fillcolor('black')
            begin_fill()
            circle(d/2)
            end_fill()
            penup()
        count += 1
    # draw little blue oval
    count = 0
    for i in range(0, 360):
        forward(step1)
        rt(1)
        if count % 18 == 5:
            pendown()
            color('dodger blue')
            begin_fill()
            # draw an oval
            len = 0
            for k in range(2):
                for j in range(60):
                    if j < 30:
                        len += step_oval
                    else:
                        len -= step_oval
                    forward(len)
                    left(3)
            end_fill()
            penup()
        count += 1
    # draw little yelllow oval
    count = 0
    for i in range(0, 360):
        forward(step1)
        rt(1)
        if count % 18 == 13:
            pendown()
            color('yellow')
            begin_fill()
            # draw an oval
            len = 0
            for k in range(2):
                for j in range(60):
                    if j < 30:
                        len += step_oval
                    else:
                        len -= step_oval
                    forward(len)
                    left(3)
            end_fill()
            penup()
        count += 1

    # relocate
    left(90)
    forward(d)
    right(90)
    pendown()

    # draw outer circle
    pencolor('white')
    pensize(0.1)
    for i in range(0, 369):
        forward(step2)
        rt(1)
    pensize(1)
    penup()

    if r_outer > 100:

        return
    else:
        return ring(r_outer)


def main():
    r = 1
    distance = 100.7
    cordinate = [
        (-3.5*distance, 2*distance), (-1.5*distance, 2*distance),
        (0.5*distance, 2*distance), (2.5*distance, 2*distance),
        (-3.5*distance, 0), (-1.5*distance, 0), (0.5*distance, 0),
        (2.5*distance, 0),
        (-3.5*distance, -2*distance), (-1.5*distance, -2*distance),
        (0.5*distance, -2*distance), (2.5*distance, -2*distance),
        (-2.5*distance, distance), (-0.5*distance, distance),
        (1.5*distance, distance),
        (-2.5*distance, -distance), (-0.5*distance, -distance),
        (1.5*distance, -distance)
    ]
    for i in cordinate:
        penup()
        goto(i)
        setheading(90)
        ring(r)
    hideturtle()
    ts = getscreen()
    ts.getcanvas().postscript(file="work2.eps")
    done()


if __name__ == '__main__':
    main()
