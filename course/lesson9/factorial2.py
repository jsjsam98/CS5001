def factorial(n):
    print('factorial(',n,'): Start')
    if n == 1:
        product = 1
    else:
        product = factorial(n-1)*n
    print('factorial(): End: returning', product)
    return product

factorial(4)