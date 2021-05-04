'''
Shangjun Jiang
CS 5001, Fall 2020
HW 8 -- Ciphers
'''
import utils


def encrypt(plaintext, key):
    """
    Function -- encrypt
        implement railfence cipher
    Parameters:
        plaintext: unencrypted data
        key: a variable as part of the algorithm
    Returns the encrypted data
    """

    if not isinstance(plaintext, str):
        raise TypeError('Plaintext should be a string')
    if not isinstance(key, int):
        raise TypeError('Key should be an int')
    if key <= 1:
        raise ValueError('Key should be greater than 1')
    plaintext = utils.strip(plaintext).upper()
    encrypt = ''
    for j in range(0, len(plaintext), 2 * key - 2):
        encrypt += plaintext[j]
    for i in range(1, key - 1):
        for j in range(len(plaintext)):
            if j % (2 * key - 2) == i or j % (2 * key - 2) == 2 * key - 2 - i:
                encrypt += plaintext[j]
    for j in range(key - 1, len(plaintext), 2 * key - 2):
        encrypt += plaintext[j]
    return encrypt


def decrypt(ciphertext, key):
    """
    Function -- decrypt
        implement railfence cipher
    Parameters:
        plaintext: encrypted data
        key: a variable as part of the algorithm
    Returns the unencrypted data
    """
    if not isinstance(ciphertext, str):
        raise TypeError('Ciphertext should be a string')
    if not isinstance(key, int):
        raise TypeError('Key should be an int')
    if key <= 1:
        raise ValueError('Key should be greater than 1')
    ciphertext = utils.strip(ciphertext).upper()
    decrypt = ''
    s = [0] * len(ciphertext)
    index = 0
    for j in range(0, len(ciphertext), 2 * key - 2):
        s[j] = ciphertext[index]
        index += 1
    for i in range(1, key - 1):
        for j in range(len(ciphertext)):
            if j % (2 * key - 2) == i or j % (2 * key - 2) == 2 * key - 2 - i:
                s[j] = ciphertext[index]
                index += 1
    for j in range(key - 1, len(ciphertext), 2 * key - 2):
        s[j] = ciphertext[index]
        index += 1

    for letter in s:
        decrypt += letter
    return decrypt