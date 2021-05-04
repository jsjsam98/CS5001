'''
Shangjun Jiang
CS 5001, Fall 2020
HW 7 -- Statistics
'''
import os


def read_data(name):
    '''
    Function -- read_data
        read data from a file
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


def average(number_list):
    '''
    Function -- average
        count the average of a list of numbers
    Parameters:
        number_list -- the list of numbers to be counted
    Returns the average number of the list
    '''

    sum = 0
    for i in number_list:
        sum += i
    average = sum/len(number_list)
    return average


def std_dev(number_list):
    '''
    Function -- std_dev
        count the standard deviation of a list
    Parameters:
        number_list -- the list of numbers to be counted
    Returns the standard deviation of the list
    '''
    mean = average(number_list)
    sum = 0
    for i in number_list:
        sum += (mean - i) ** 2
    std = (sum/(len(number_list) - 1)) ** 0.5
    return std


def t_test(list1, list2):
    '''
    Function -- t_test
        count the studnet's t_test of a list
    Parameters:
        number_list -- the list of numbers to be counted
    Returns the t_test of the list
    '''
    x1 = average(list1)
    x2 = average(list2)
    s1 = std_dev(list1)
    s2 = std_dev(list2)
    n1 = len(list1)
    n2 = len(list2)
    t_test = (x1 - x2) / (((s1 ** 2) / n1 + (s2**2) / n2)) ** 0.5
    return t_test


def degrees_of_freedom(list1, list2):
    '''
    Function -- degrees_of_freedom
        count the degree of freedom of a list
    Parameters:
        number_list -- the list of numbers to be counted
    Returns the degree of freedom of the list
    '''
    s1 = std_dev(list1)
    s2 = std_dev(list2)
    n1 = len(list1)
    n2 = len(list2)
    a = ((s1 ** 2) / n1 + (s2 ** 2) / n2) ** 2
    b = (((s1 ** 2) / n1) ** 2) / (n1 - 1) + (((s2 ** 2) / n2) ** 2) / (n2 - 1)
    f = a / b
    return f


def main():
    filename1 = input('Enter file name for first data set: ')
    filename2 = input('Enter file name for second data set: ')

    number_list1 = read_data(filename1)
    number_list2 = read_data(filename2)

    t = t_test(number_list1, number_list2)
    freedom = degrees_of_freedom(number_list1, number_list2)
    print('t =', t)
    print('f =', freedom)


if __name__ == "__main__":
    main()
