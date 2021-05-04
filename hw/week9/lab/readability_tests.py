'''
Shangjun Jiang
CS 5001, Fall 2020
Lab 10 test -- readability_tests

This is a test program
'''
import os
from readability import *


def test_flesch_grade(index, result):
    outcome = flesch_grade(index)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_flesch_index(sentences, words, syllables, result):
    outcome = flesch_index(sentences, words, syllables)
    outcome = float(format(outcome, '.1f'))
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_count_syllables(words, result):
    outcome = count_syllables(words)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_analyze_file_data(file_data, result):
    outcome = analyze_file_data(file_data)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def main():
    #  test for flesch_grade
    print('...start testing flesch_grade')
    test_flesch_grade(-1, 'Law school graduate')
    test_flesch_grade(99, '5th Grader')

    #  test for flesch_index
    print('...start testing flesch_index')
    test_flesch_index(2, 29, 37, 84.2)
    test_flesch_index(11, 282, 400, 60.8)

    #  test for count_syllables
    print('...start testing count_syllables')
    test_count_syllables('you', 1)
    test_count_syllables('me', 1)
    test_count_syllables('university,', 5)

    #  test for analyze_file_data
    print('...start testing analyze_file_data')
    test_analyze_file_data('school', (0, 1, 1))
    test_analyze_file_data('Flesch invented a simple tool to estimate\
    the legibility of a document without linguistic analysis.', (1, 15, 31))


if __name__ == '__main__':
    main()
