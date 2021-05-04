'''
Shangjun Jiang
CS 5001, Fall 2020
Module 7 Lab -- Sequences & for Loops

This is program  receives a list and returns a new list
that contains every other element of the argument
'''


def every_other(initial_list):
    '''
    Function -- normalize
        the function receives a non-void list
    Parameters:
        initial_list -- the original list of elements
    Returns  a new list that contains every other element of the argument
    '''
    length = len(initial_list)
    new_list = []
    for i in range(0, length, 2):
        new_list.append(initial_list[i])
    return new_list


def main():

    print('...start test')
    test_pass_num = 0

    # test 1
    list_1 = [1, 2, 3, 4, 5, 6]
    test_result = every_other(list_1)
    print('Expected outcome:', [1, 3, 5])
    print('Actual outcome:', test_result)
    if test_result == [1, 3, 5]:
        test_pass_num += 1
        print('Success! {}/3'.format(test_pass_num))
    else:
        print('Fail!')

    # test 2
    list_2 = ['a', 'b', 'c', 'd', 'e']
    test_result = every_other(list_2)
    print('Expected outcome:', ['a', 'c', 'e'])
    print('Actual outcome:', test_result)
    if test_result == ['a', 'c', 'e']:
        test_pass_num += 1
        print('Success! {}/3'.format(test_pass_num))
    else:
        print('Fail!')

    # test 3
    list_3 = [['this is a list'], 'this is string', 5, 3, 'test3']
    test_result = every_other(list_3)
    print('Expected outcome:', [['this is a list'], 5, 'test3'])
    print('Actual outcome:', test_result)
    if test_result == [['this is a list'], 5, 'test3']:
        test_pass_num += 1
        print('Success! {}/3'.format(test_pass_num))
    else:
        print('Fail!')


if __name__ == '__main__':
    main()
