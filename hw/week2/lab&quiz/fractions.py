import math


def main():
    value = float(input('Enter a value: '))
    a = math.floor(value)
    b = int((value-a)*100)
    print('{} ~= {} {}/100'.format(value, a, b))


if __name__ == '__main__':
    main()
