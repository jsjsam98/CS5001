'''
CS5001 Shangjun Jiang
Fall 2020
'''


def is_palindrome(msg):
    '''Reads a string and judge if it is palindrome'''
    length = len(msg)
    i = 0
    while i < length//2:
        if msg[i] == msg[length-i-1]:
            i += 1
        else:
            return False
    return True


def main():
    test1 = is_palindrome('Northeastern')
    print('test1:\n', test1)
    test2 = is_palindrome('NortroN')
    print('test2:\n', test2)
    test3 = is_palindrome('1234321')
    print('test3:\n', test3)
    test4 = is_palindrome('123321')
    print('test4:\n', test4)


if __name__ == '__main__':
    main()
