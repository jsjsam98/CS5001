def numbers(value):

    if value == 0:
        print('Done!')
        return
    else:
        print(value)
        return numbers(value-1)
