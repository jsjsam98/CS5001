'''
CS5001 Shangjun Jiang
Fall 2020
'''


def reorganize(words):
    '''reorganize a string by putting vowels in the front'''
    if type(words) != str:
        return('Type error!')
    length = len(words)
    i = 0

    vowel = ''
    consonant = ''
    while i < length:
        if words[i] == 'a' or words[i] == 'e' or\
                words[i] == 'i' or words[i] == 'o' or\
                words[i] == 'u' or words[i] == 'y' or\
                words[i] == 'A' or words[i] == 'E' or\
                words[i] == 'I' or words[i] == 'O' or\
                words[i] == 'U' or words[i] == 'Y':
            vowel += words[i]
        else:
            consonant += words[i]
        i += 1
    str_reorganize = vowel+consonant
    return str_reorganize


def main():
    test1 = reorganize('Northeastern')
    print('test1:\n', test1)
    test2 = reorganize(404)
    print('test2:\n', test2)
    test3 = reorganize('ABCdefuio')
    print('test3:\n', test3)


if __name__ == '__main__':
    main()
