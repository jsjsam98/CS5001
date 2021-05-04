'''
Shangjun Jiang
CS 5001, Fall 2020
Module 7 Lab -- Sequences & for Loops

This is a list partition program
'''


def partition(list1, list2, list3):
    '''
    Function -- normalize
        non-void list
    Parameters:
        list1 -- a list of numerical values
        list2 -- a list of numerical values
        list3 -- a list of numerical values
    Returns the number of elements of the first
            list that are not in either list.
    '''
    number = 0
    for i in list1:
        if i < 0:
            list2.append(i)
        elif i > 0:
            list3.append(i)
    for i in list1:
        if i in list2:
            pass
        elif i in list3:
            pass
        else:
            number += 1
    return number


def main():

    print('...start test')
    test_pass_num = 0

    # test 1
    list_1 = [0, 1, 2, 3, 4, 5, 6]
    list_2 = [7, 8, 9]
    list_3 = []
    test_result = partition(list_1, list_2, list_3)
    print('Expected outcome:', 1)
    print('Actual outcome:', test_result)
    if test_result == 1:
        test_pass_num += 1
        print('Success! {}/2'.format(test_pass_num))
    else:
        print('Fail!')

    # test 2
    list_1 = [2, 3, 4, 5, -6]
    list_2 = [7, 8, 9]
    list_3 = []
    test_result = partition(list_1, list_2, list_3)
    print('Expected outcome:', 0)
    print('Actual outcome:', test_result)
    if test_result == 0:
        test_pass_num += 1
        print('Success! {}/2'.format(test_pass_num))
    else:
        print('Fail!')


if __name__ == '__main__':
    main()
