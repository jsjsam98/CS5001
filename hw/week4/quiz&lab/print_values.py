def print_values():
    initial_number = float(input('Please enter a number: \n'))
    i = 1
    done = False
    while not done:
        multi = i*initial_number
        print('{}*{}={}'.format(i, initial_number, multi))
        i += 1
        if i > 10:
            done = True
