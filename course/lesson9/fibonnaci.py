''' Align Online
    CS5001
    Sample code for Module 9: Recursion.
    Two implementations of a function that calculates the nth Fibonnaci number.
'''


def fib(n):
    '''
    function: fib, an iterative solution for calculating the nth Fibonnaci
    param:    positive integer, the Fibonnaci number to calculate
    return:   the nth Fibonnaci number
    '''
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        i = 1
        current = 1
        previous = 1
        while n > i:
            i += 1
            next = previous + current
            previous = current
            current = next
        result = current
    return result


def r_fib(n):
    '''
    function: r_fib, a recursive solution for calculating the nth Fibonnaci
    param:    positive integer, the Fibonnaci number to calculate
    return:   the nth Fibonnaci number
    '''
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = r_fib(n - 2) + r_fib(n - 1)
    return result

number = r_fib(10)
print(number)