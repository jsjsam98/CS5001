"""
Module: Handing Exceptions

This is the code that we are starting with in module 10.  Many changes 
will be made to the code and there will be a couple of different version
as we cover the material in this module.

Version 2 include the validation of the parameters in get_slices
"""


def get_slices(pies, folks):
    ''' Function: get_slices that calculates the number of slices of pizza
        Params:   pies, the number of pies
                  folks, the number of people
        Returns:  the number of slices per person
    '''
    if not isinstance(folks, int) or folks <= 0:
        raise ValueError("folks must be a positive integer")
    if not isinstance(pies, int):
        raise TypeError("pies must be an integer value")
    if pies < 0:
        raise ValueError("pies must be non-negative integer")
    # multiply by 8 slices per pie and divide
    slices = pies * 8 // folks
    return slices


def main():
    # get two integers from the user
    pizzas = int(input("How many pizzas did you order? "))
    people = int(input("How many people are there? "))
    slices = get_slices(pizzas, people)
    print(pizzas, "pizzas split", people, "ways is", slices, "slices each")


main()
