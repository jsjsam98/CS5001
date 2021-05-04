'''
CS5001 Shangjun Jiang
Fall 2020
'''


def filter_list(list_int, option):
    '''divide a numeric list into positive and negative part'''
    length = len(list_int)
    i = 0
    positive_list = []
    negative_list = []
    while i < length:
        if list_int[i] > 0:
            positive_list.append(list_int[i])
        elif list_int[i] < 0:
            negative_list.append(list_int[i])
        i += 1
    if type(option) != bool:
        return 'Type error! The second argument should be boolen.'
    else:
        if option is True:
            return positive_list
        else:
            return negative_list


def main():
    test1 = filter_list([1, -2, 3, -4, 5, -6, 7, -8], True)
    print('test1:\n', test1)
    test2 = filter_list([1, -2, 3, -4, 5, -6, 7, -8], False)
    print('test2:\n', test2)
    test3 = filter_list([1, -2, 3, -4, 5, -6, 7, -8], 10)
    print('test3:\n', test3)


if __name__ == '__main__':
    main()
