'''
Shangjun Jiang
CS 5001, Fall 2020
Lab 10 -- readability

This is a Flesch readability index program
'''
import os


def analyze_file_data(file_data):
    '''
    Function: analyze_file_data
       Calculates the number of sentences, words, and syllabues in file_data
    Parameters:
       file_data -- the data to analyze
    Returns the number of sentences (int), the number of words (int),
       and the number of syllables in file_data
    '''
    sentences = 0
    words = 0
    syllables = 0
    sentence_seperate = ['.', '?', '!', ':', ';']
    strip_list = [',', '.', '?', '!', ':', ';']
    msg = ''
    for i in file_data:
        msg += i

    for i in msg:
        if i in sentence_seperate:
            sentences += 1

    words_list = msg.split()
    words = len(words_list)

    for i in words_list:
        for j in strip_list:
            i = i.strip(j)
        syllables += count_syllables(i)

    return sentences, words, syllables


def count_syllables(word):
    '''
    Function: count_syllables
       Counts the total number of syllables in the provided word
    Parameters:
       word -- the word that we want to count the syllables of
    Returns the number of syllables in the word
    '''
    # TODO: implement me!
    if isinstance(word, str):
        word = str(word)
    else:
        raise TypeError('word should be a str')
    syllables = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u',
                  'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    flag = False
    length = len(word)
    for j in range(length-1):
        if word[j] in vowel_list and word[j+1] not in vowel_list:
            syllables += 1
            flag = True

    if word[length-1] in vowel_list and word[length-1] != 'e':
        syllables += 1
        flag = True

    if flag is False:
        syllables += 1

    return syllables


def flesch_index(sentences, words, syllables):
    '''
    Function: flesch_index
       calculates the Flesch readability index
    Parameters:
       sentences (int) -- the number of sentences in a document
       words (int) -- the number of words in a document
       syllables (int) -- the number of syllables
    Returns the Flesch readability index calculated by the provided formula
    '''
    return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)


def flesch_grade(index):
    '''
    Function: flesch_grade
       Caclulates the Flesch grade (educational level)
    Parameters:
       index (float) -- Flesch readability index
    Returns the educational level
    '''
    # TODO: Implement me!!
    if isinstance(index, float):
        index = float(index)
    else:
        raise TypeError('Index should be a float')

    if index < 0.0:
        flesch_grade = 'Law school graduate'
    elif index <= 29.9 and index >= 0.0:
        flesch_grade = 'College graduate'
    elif index <= 49.9 and index >= 30.0:
        flesch_grade = 'College'
    elif index <= 64.9 and index >= 50:
        flesch_grade = 'High schooler'
    elif index <= 69.9 and index >= 65:
        flesch_grade = '8th Grader'
    elif index <= 79.9 and index >= 70.0:
        flesch_grade = '7th Grader'
    elif index <= 89.9 and index >= 80.0:
        flesch_grade = '6th Grader'
    elif index <= 100 and index >= 90:
        flesch_grade = '5th Grader'
    else:
        # actually should be under 5th Grader
        # according to codepost
        flesch_grade = '5th Grader'
    return flesch_grade


def main():
    """ The main driver of the program. """
    # Ask user for name of file to analyze.
    done = False
    while not done:
        try:
            filename = input("Filename: ")

            # Open file for reading.
            input_file = open(filename, 'r')
            # decide if the work is done
            done = True

            # Read all of the contents of the file
            # into a list of strings called filedata.
            filedata = input_file.readlines()

            # Analyze the data from the file to calculate
            # the number of sentences, the number of words
            # and the number of syllables in the file
            sentences, words, syllables = analyze_file_data(filedata)
            index = flesch_index(sentences, words, syllables)
            grade = flesch_grade(index)

            # Close the file.
            input_file.close()

            # Output result.
            print()
            print("Sentences:", sentences)
            print("Words:", words)
            print("Syllables:", syllables)
            print()
            print("Words per Sentence: {0:.1f}".format(words / sentences))
            print("Syllables per Word: {0:.1f}".format(syllables / words))
            print()
            print("Flesch Index: {0:.1f}".format(index))
            print("Flesch Grade:", grade)

        except FileNotFoundError:
            print("{} does not exist".format(filename))
        except PermissionError:
            print("You do not have sufficient permissions to open {}"
                  .format(filename))
        except OSError:
            print("An unexpected error occurred while attempting to open {}"
                  .format(filename))


if __name__ == '__main__':
    main()
