'''
CS5001 Shangjun Jiang
Fall 2020
'''


def mix_up(string1, string2):
    '''Read two strings of equal length and mix them together'''
    if type(string1) != str or type(string2) != str:
        return('Type error!')
    if len(string1) == len(string2):
        length = len(string1)
        i = 0
        mix_str = ''
        while i < length:
            mix_str += string1[i]+string2[i]
            i += 1
        return mix_str
    else:
        return('The strings given are not equal length!')


def main():
    test1 = mix_up('hello', 'world')
    print('test1:\n', test1)

    test2 = mix_up('ni', 'hao')
    print('test2\n', test2)

    test3 = mix_up('ni', 123)
    print('test3\n', test3)


if __name__ == '__main__':
    main()
