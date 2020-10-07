'''
CS5001 Shangjun Jiang
Fall 2020
'''


def spread_string(list_msg, num_spaces):
'''
    This funtion prints a list of strings in which each letter 
    of the string are spilt with the given number of spaces
'''
    length_list = len(list_msg)
    i = 0
    while i < length_list:
        length_string = len(list_msg[i])
        j = 0
        msg = ''
        while j < length_string-1:
            msg += list_msg[i][j]+' '*num_spaces
            j += 1
        msg += list_msg[i][j]
        print(msg)
        i += 1
