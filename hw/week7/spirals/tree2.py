from turtle import *

def draw_tree(length):
    right(20)
    fd(length)


color('#5E5E5E')
pensize(5)

penup()
goto(0,-300)
pendown()

left(80)
fd(140)
draw_tree(60)
done()