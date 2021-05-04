'''
Shangjun Jiang
CS 5001, Fall 2020
HW 7 -- Statistics (test)

This is a test program
'''

from analysis import *
import statistics
import os


def read_data(name):
    '''
    Function -- read_data
        Use the function to read the data for test
    Parameters:
        name -- the filename
    Returns a list of numbers in the file line by line
    '''
    try:
        file = open(name, 'r')
        content = file.readlines()
        number_list = []
        for i in content:
            i = int(i.strip())
            number_list.append(i)
        file.close()
    except FileNotFoundError:
        raise ValueError('Could not read {}, file was not found'.format(name))
    except PermissionError:
        raise ValueError('Could not read {}, permission error'.format(name))
    except OSError:
        raise ValueError('OSError occurred while reading {}'.format(name))
    return number_list


def test_average(number_list):
    '''
    Function -- test_average
        test the average function
    Parameters:
        number_list -- the list of numbers to be counted
    Prints Pass if it succeed
    '''
    average1 = average(number_list)
    average2 = statistics.mean(number_list)
    if average1 == average2:
        print('Pass')
    else:
        print('Fail')


def test_std_dev(number_list):
    '''
    Function -- test_std_dev
        test the std_dev function
    Parameters:
        number_list -- the list of numbers to be counted
    Prints Pass if it succeed
    '''
    std1 = std_dev(number_list)
    std2 = statistics.stdev(number_list)
    if (std1 - std2) < 0.00001:
        print('Pass')
    else:
        print('Fail')


def main():
    list1 = read_data('input_a.txt')
    list2 = read_data('input_b.txt')
    list3 = read_data('input_c.txt')
    print('start testing function average...')
    test_average(list1)
    test_average(list2)
    test_average(list3)
    print('start testing function std_dev...')
    test_std_dev(list1)
    test_std_dev(list2)
    test_std_dev(list3)


if __name__ == '__main__':
    main()
