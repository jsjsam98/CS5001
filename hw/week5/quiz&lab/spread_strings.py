'''
Shangjun Jiang
CS 5001, Fall 2020
Module 6 Quiz

This is a subway guideline program
'''


def spread_string(list_msg, num_spaces):
    '''
    Function -- spread_string
        spread words in a list of string by spaces
    Parameters:
        list_msg -- a list of words
        num_spaces -- number of spaces
    Print each string out on its own line with spaces bewteen letters
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
        msg += list_msg[i][j]  # avoid printing an extra whitespace at the end
        print(msg)
        i += 1


spread_string(['abcd', 'efghijk', 'lmnopq'], 1)
