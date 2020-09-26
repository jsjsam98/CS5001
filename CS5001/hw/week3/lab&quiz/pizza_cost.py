def pizza_cost(diameter, price):
    area = 3.14159*(float(diameter)/2)**2
    cost_per_square = float(price)/area
    return cost_per_square


def main():
    diameter = input('Enter the diameter of pizza: ')
    price = input('Enter the price of pizza: ')
    cost_per_square = pizza_cost(diameter, price)
    print('The cost per square is:', cost_per_square)


if __name__ == '__main__':
    main()
