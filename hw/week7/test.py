from turtle import *

def main():
    s=Shape('compound')
    poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
    s.addcomponent(poly1, "red", "blue")
    poly2 = ((0,0),(10,-5),(-10,-5))
    s.addcomponent(poly2, "blue", "red")
    register_shape('myshape',s)
    shape('myshape')

    done()
if __name__ == '__main__':
    main()