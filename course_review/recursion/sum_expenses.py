''' Align Online
    CS5001
    Sample code for Module 9: Recursion.
    Function calculates the sum of charages and returns it.
'''


def sum_expenses(charges):
    """ 
    sum_expenses: calculates the sum of all the charges. 
    params: a list of charges
    returns: the sum of all the charges
    """
    sum = 0
    for i in range(len(charges)):
        if isinstance(charges[i], list):
            sum += sum_expenses(charges[i])
        else:
            sum += charges[i]
        print("DEBUG: i =", i, ", sum =", sum)
    return sum


# a simple list of expenses
receipts = [10, 11, 10, 11, 13]

# a nested list of expenses
nested_receipts = [10, 11, [6, 2, 2], 11, 13]

# a nested list of nested lists of expenses
ugly_receipts = [1, 2, [3, 4, [5, 6, [7, 6, 8]]]]
