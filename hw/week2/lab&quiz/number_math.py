def main():
    first_num = int(input('Enter first number: '))
    second_num = int(input('Enter second number: '))

    if first_num < second_num:

        Product = first_num*second_num
        print('Product is {}'.format(Product))

    elif first_num == second_num:
        Square = first_num**2
        print('Square is {}'.format(Square))

    else:
        Sum = first_num+second_num
        print('Sum is {}'.format(Sum))


if __name__ == '__main__':
    main()
