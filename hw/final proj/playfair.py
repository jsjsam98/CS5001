'''
Shangjun Jiang
CS 5001, Fall 2020
HW 8 -- Ciphers
'''
import utils


def encrypt(plaintext, key):
    """
    Function -- encrypt
        implement playfair cipher
    Parameters:
        plaintext: unencrypted data
        key: a variable as part of the algorithm
    Returns the encrypted data
    """
    if not isinstance(plaintext, str):
        raise TypeError('Plaintext should be a string')
    if not isinstance(key, str):
        raise TypeError('Key should be a string')
    plaintext = utils.strip(plaintext).upper()
    key = utils.strip(key).upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                'X', 'Y', 'Z']
    encrypt = ''
    key = key.upper()
    key_list = []
    for i in key:
        if i not in key_list:
            key_list.append(i)

    key_list = ['I' if x == 'J' else x for x in key_list]

    for i in alphabet:
        if i not in key_list:
            key_list.append(i)

    plainlist = list(plaintext)
    plainlist = ['I' if x == 'J' else x for x in plainlist]
    length = len(plainlist)

    index = 0
    while index < length - 1:
        first = plainlist[index]
        second = plainlist[index + 1]
        if first == second:
            plainlist[index+1] = 'X'
        index += 1

    if length % 2 == 1:
        plainlist.append('X')

    index = 0
    while index < length:
        first = plainlist[index]
        second = plainlist[index + 1]
        row1 = key_list.index(first) // 5
        column1 = key_list.index(first) % 5
        row2 = key_list.index(second) // 5
        column2 = key_list.index(second) % 5

        if row1 != row2 and column1 != column2:
            first_cipher = key_list[row1 * 5 + column2]
            second_cipher = key_list[row2 * 5 + column1]
            encrypt += first_cipher + second_cipher
        elif row1 == row2:
            first_cipher = key_list[row1 * 5 + (column1 + 1) % 5]
            second_cipher = key_list[row2 * 5 + (column2 + 1) % 5]
            encrypt += first_cipher + second_cipher
        elif column1 == column2:
            first_cipher = key_list[((row1 + 1) % 5) * 5 + column1]
            second_cipher = key_list[((row2 + 1) % 5) * 5 + column2]
            encrypt += first_cipher + second_cipher
        index += 2

    return encrypt


def decrypt(ciphertext, key):
    """
    Function -- decrypt
        implement playfair cipher
    Parameters:
        plaintext: encrypted data
        key: a variable as part of the algorithm
    Returns the unencrypted data
    """
    if not isinstance(ciphertext, str):
        raise TypeError('Ciphertext should be a string')
    if not isinstance(key, str):
        raise TypeError('Key should be a string')
    key = utils.strip(key).upper()
    ciphertext = utils.strip(ciphertext).upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                'X', 'Y', 'Z']
    decrypt = ''
    key = key.upper()
    key_list = []
    for i in key:
        if i not in key_list:
            key_list.append(i)

    key_list = ['I' if x == 'J' else x for x in key_list]

    for i in alphabet:
        if i not in key_list:
            key_list.append(i)

    cipherlist = list(ciphertext)
    length = len(cipherlist)
    index = 0

    while index < length:
        first = cipherlist[index]
        second = cipherlist[index + 1]
        row1 = key_list.index(first) // 5
        column1 = key_list.index(first) % 5
        row2 = key_list.index(second) // 5
        column2 = key_list.index(second) % 5

        if row1 != row2 and column1 != column2:
            first_cipher = key_list[row1 * 5 + column2]
            second_cipher = key_list[row2 * 5 + column1]
            decrypt += first_cipher + second_cipher
        elif row1 == row2:
            first_cipher = key_list[row1 * 5 + (column1 + 4) % 5]
            second_cipher = key_list[row2 * 5 + (column2 + 4) % 5]
            decrypt += first_cipher + second_cipher
        elif column1 == column2:
            first_cipher = key_list[((row1 + 4) % 5) * 5 + column1]
            second_cipher = key_list[((row2 + 4) % 5) * 5 + column2]
            decrypt += first_cipher + second_cipher
        index += 2
    return decrypt