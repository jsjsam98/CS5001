'''
CS5001 Shangjun Jiang
Fall 2020
'''


def max_value(list_values):
'''
    This funtion prints the max value in the given 
    list using guess-and-check method!
'''
    length = len(list_values)
    i = 1
    num_larger = list_values[0]
    while i < length:
        num_less = list_values[i]
        if num_larger < num_less:
            num_larger = num_less
        else:
            pass
        i += 1
    print(num_larger)
