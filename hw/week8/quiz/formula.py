def formula(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return 2 * formula(n - 1) + formula(n - 2)
