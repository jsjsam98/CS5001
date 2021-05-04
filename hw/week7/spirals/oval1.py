from turtle import *
speed(0)
tracer(0, 0)
len = 0
color('red','green')
begin_fill()
for i in range (18):
    pendown()
    # draw an oval
    for k in range(2):       
        for j in range(90):
            if j < 45:
                len += 0.1
            else:
                len -= 0.1
            forward(len)
            left(2)
    rt(20)
end_fill()
penup()
home()
pendown()
color('blue','yellow')
circle(200)
done()