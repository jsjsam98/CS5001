from turtle import *


def main():
    bgcolor('black')
    speed(0)
    tracer(0)
    i = 1
    colours = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
    while True:
        width(5)
        forward(i)
        left(100)
        color(colours[i % 7])
        i += 1
        if i == 500:
            break
    ts = getscreen()
    ts.getcanvas().postscript(file="work3.eps")
    hideturtle()
    done()


if __name__ == '__main__':
    main()
