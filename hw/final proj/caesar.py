''''
Shangjun Jiang
CS 5001, Fall 2020
HW 8 -- Ciphers
'''
import utils


def encrypt(plaintext, key):
    """
    Function -- encrypt
        implement caesar cipher
    Parameters:
        plaintext: unencrypted data
        key: a variable as part of the algorithm
    Returns the encrypted data
    """
    if not isinstance(plaintext, str):
        raise TypeError('Plaintext should be a string')
    if not isinstance(key, int):
        raise TypeError('Key should be an int')

    plaintext = utils.strip(plaintext).upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']
    encrypt = ''

    for i in plaintext:
        index = alphabet.index(i)
        new_index = (index + key) % 26
        encrypt += alphabet[new_index]
    return encrypt


def decrypt(ciphertext, key):
    """
    Function -- decrypt
        implement caesar cipher
    Parameters:
        plaintext: encrypted data
        key: a variable as part of the algorithm
    Returns the unencrypted data
    """
    if not isinstance(ciphertext, str):
        raise TypeError('Ciphertext should be a string')
    if not isinstance(key, int):
        raise TypeError('Key should be an int')

    ciphertext = utils.strip(ciphertext).upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']
    decrypt = ''
    for i in ciphertext:
        index = alphabet.index(i)
        new_index = (index - key) % 26
        decrypt += alphabet[new_index]
    return decrypt