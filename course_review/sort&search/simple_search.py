''' Align Online CS5001
    Module 14 -- Efficiency 
    Sample code -- example of a simple search
'''

# a list of names that we can use when we run my_search
names = ["Amy", "Bob", "Carol", "David", "Ellie", "Frank"]


def my_search(name, my_list):
    '''
    Function: my_search -- do a linear search through the list
    Parameters:
       name -- the name we are looking for
       my_list -- the list we are looking through
    Returns the index of the name in the list, or -1 if it is not there
    '''
    for i in range(len(my_list)):
        if my_list[i] == name:
            return i
    return -1
