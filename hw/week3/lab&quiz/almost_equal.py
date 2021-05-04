import math


def almost_equal(a, b):
    d = math.fabs(a-b)
    if d <= 0.001:
        return True
    else:
        return False


def main():
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    boolvalue = almost_equal(a, b)
    print(boolvalue)


if __name__ == '__main__':
    main()
