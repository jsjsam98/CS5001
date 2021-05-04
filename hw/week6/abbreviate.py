'''
Shangjun Jiang
CS 5001, Fall 2020
Module 7 Lab -- Sequences & for Loops

This is program receives a word as an argument
and returns a new string that has all the vowels removed.
'''


def abbreviate(word):
    '''
    Function -- normalize
        receive a word
    Parameters:
        word -- the original string of a word
    Returns a new string with vowels removed
    '''
    length = len(word)
    new_word = ''
    for i in range(0, length):
        letter = word[i]
        if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            pass
        else:
            new_word += letter
    return new_word


def main():

    print('...start test')
    test_pass_num = 0

    # test 1
    word_1 = 'happiness'
    test_result = abbreviate(word_1)
    print('Expected outcome:', 'hppnss')
    print('Actual outcome:', test_result)
    if test_result == 'hppnss':
        test_pass_num += 1
        print('Success! {}/3'.format(test_pass_num))
    else:
        print('Fail!')

    # test 2
    word_2 = 'Awesome'
    test_result = abbreviate(word_2)
    print('Expected outcome:', 'wsm')
    print('Actual outcome:', test_result)
    if test_result == 'wsm':
        test_pass_num += 1
        print('Success! {}/3'.format(test_pass_num))
    else:
        print('Fail!')

    # test 3
    word_3 = 'AaBbCcDdEe'
    test_result = abbreviate(word_3)
    print('Expected outcome:', 'BbCcDd')
    print('Actual outcome:', test_result)
    if test_result == 'BbCcDd':
        test_pass_num += 1
        print('Success! {}/3'.format(test_pass_num))
    else:
        print('Fail!')


if __name__ == '__main__':
    main()
