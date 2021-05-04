'''
Shangjun Jiang
CS 5001, Fall 2020
Module 7 Lab -- Sequences & for Loops

This is program receives a list of integer values
and returns the sum of all of the even numbers in the list.
'''


def even_sum(int_list):
    '''
    Function -- normalize
        non-void list
    Parameters:
        int_list -- a list of integer values
    Returns the sum of all even numbers
    '''

    sum_even_num = 0
    for i in int_list:
        if i % 2 == 0:
            sum_even_num += i
        else:
            pass
    return sum_even_num


def main():

    print('...start test')
    test_pass_num = 0

    # test 1
    list_1 = [1, 2, 3, 4, 5, 6]
    test_result = even_sum(list_1)
    print('Expected outcome:', 12)
    print('Actual outcome:', test_result)
    if test_result == 12:
        test_pass_num += 1
        print('Success! {}/2'.format(test_pass_num))
    else:
        print('Fail!')

    # test 2
    list_2 = [1, 1, 2, 2, 2]
    test_result = even_sum(list_2)
    print('Expected outcome:', 6)
    print('Actual outcome:', test_result)
    if test_result == 6:
        test_pass_num += 1
        print('Success! {}/2'.format(test_pass_num))
    else:
        print('Fail!')


if __name__ == '__main__':
    main()
