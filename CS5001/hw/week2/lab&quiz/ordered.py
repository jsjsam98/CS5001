def main():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    c = int(input('Enter third number: '))
    if (a >= b and a >= c and b >= c):
        x1 = a
        x2 = b
        x3 = c
    elif (a >= b and a >= c and b <= c):
        x1 = a
        x2 = c
        x3 = b
    elif (b >= a and b >= c and a >= c):
        x1 = b
        x2 = a
        x3 = c
    elif (b >= a and b >= c and a <= c):
        x1 = b
        x2 = c
        x3 = a
    elif (c >= b and c >= a and a >= b):
        x1 = c
        x2 = a
        x3 = b
    elif (c >= b and c >= a and a <= b):
        x1 = c
        x2 = b
        x3 = a

    else:
        print('program wrong')

    print('{}, {}, {}'.format(x1, x2, x3))


if __name__ == '__main__':
    main()
