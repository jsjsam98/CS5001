''' Align Online
    CS5001
    Sample code for Module 9: Recursion.
    Two implementations of a function that calculates the factorial of n.
'''

def factorial(n):
    '''
    function: factorial, an iterative solution for calculating the factorial
    param:    positive integer, to calculate the factorial of
    return:   the factorial of n
    '''
    i = 1
    product = 1
    while i <= n:
        product *= i
        i += 1
    return product


def r_factorial(n):
    '''
    function: r_factorial, a recursive solution for calculating the factorial
    param:    positive integer, to calculate the factorial of
    return:   the factorial of n
    '''
    if n == 1:
        return 1
    else:
        product = r_factorial(n - 1) * n
    return product
