'''
Shangjun Jiang
CS 5001, Fall 2020
Lab 11 -- scrabble_tests

This is a test for scrabble game program.
'''

from scrabble import *


def test_store_words(file_data, result):
    '''
    Function -- test_store_words
        test the function and print Pass if it succeed
    Parameters:
        file_data -- a list of strings containing the words to be sorted
        result -- the expected result
    Prints the result on the screen
    '''
    outcome = store_words(file_data)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_get_words(max_length, word_dict, letters, result):
    '''
    Function -- test_get_words
        test the function and print Pass if it succeed
    Parameters:
        letters -- letters that the words should contain
        word_dict -- With length of words as key and the words as values
        max_length -- maximum length of the word to be displayed
    Print the result on the screen
    '''
    outcome = get_words(max_length, word_dict, letters)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_get_scores(words, result):
    '''
    Function -- test_get_scores
        test the function and print Pass if it succeed
    Parameters:
        words -- List of words containing the user input letters
        results -- number of highest scoring words to display
    Print the result on the screen
    '''
    outcome = get_scores(words)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def main():
    # enumerate the data for test
    file_data1 = ['a', 'b', 'cd']
    file_data2 = ['quiz', 'quizzer']
    print('start testing store_words...')
    test_store_words(file_data1, {1: ['a', 'b'], 2: ['cd']})
    test_store_words(file_data2, {4: ['quiz'], 7: ['quizzer']})

    file_data = read_text_file()
    word_dict = store_words(file_data)
    max_length = 7
    print('start testing get_words...')

    test_get_words(max_length, word_dict, 'quize', [
                   'bezique', 'cazique', 'mezquit', 'quizzed',
                   'quizzer', 'quizzes'])

    print('start testing get_scores...')
    test_get_scores(['a'], {1: ['a']})
    test_get_scores(['abc', 'kd'], {7: ['abc', 'kd']})


if __name__ == '__main__':
    main()
