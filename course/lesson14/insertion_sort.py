''' Align Online CS5001
    Module 14 -- Efficiency
    Sample code -- implementation of insertion sort
'''
import random


def insertion_sort(things):
    '''
    Function: insertion_sort -- sorting the elements of a list by inserting
                                each element into a list in order
    Parameters:
       things -- the elements to be sorted
    Returns a new list with all of the elements in sorted order
    '''
    sorted = list()
    for item in things:
        # find the correct position to insert this value
        for i in range(len(sorted) + 1):
            if i == len(sorted) or item < sorted[i]:
                # copies all the values to make room for the new one
                sorted.insert(i, item)
                break
    return sorted


def main():
    '''
    Function: main -- driver program for insertion_sort
    '''
    my_list = [i for i in range(100)]
    random.shuffle(my_list)
    print(my_list)
    sorted_list = insertion_sort(my_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
