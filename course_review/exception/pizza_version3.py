"""
Module: Handing Exceptions

This is the code that we are starting with in module 10.  Many changes 
will be made to the code and there will be a couple of different version
as we cover the material in this module.

Version 3 include the validation of the parameters in get_slices, 
and uses validates the keyboard input in main
"""


def get_slices(pies, folks):
    ''' Function: get_slices that calculates the number of slices of pizza
        Params:   pies, the number of pies
                  folks, the number of people
        Returns:  the number of slices per person
    '''
    if not isinstance(folks, int):
        raise TypeError("folks must be an integer")
    if folks <= 0:
        raise ValueError("folks must be positive")
    if not isinstance(pies, int):
        raise TypeError("pies must be an integer")
    if pies < 0:
        raise ValueError("pies must be non-negative")
    slices = pies * 8 // folks
    return slices


def main():
    while pizzas < 0:
        pizzas_text = input("How many pizzas did you order? ")
        if pizzas_text.isnumeric():
            pizzas = int(pizzas_text)

    people = -1
    while people <= 0:
        people_text = input("How many people are there? ")
        if people_text.isnumeric():
            people = int(people_text)

    slices = get_slices(pizzas, people)
    print(pizzas, "pizzas split", people, "ways is", slices, "slices each")


main()
