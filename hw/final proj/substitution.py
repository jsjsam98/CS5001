'''
Shangjun Jiang
CS 5001, Fall 2020
HW 8 -- Ciphers
'''
import utils


def encrypt(plaintext, key):
    """
    Function -- encrypt
        implement substitution cipher
    Parameters:
        plaintext: unencrypted data
        key: a variable as part of the algorithm
    Returns the encrypted data
    """

    if not isinstance(plaintext, str):
        raise TypeError('Plaintext should be a string')
    if plaintext == '':
        raise ValueError('Plaintext can not be empty')
    if not isinstance(key, str):
        raise TypeError('Key should be a string')
    if len(key) != 26:
        raise ValueError('Key should be at the length of 26')
    for i in plaintext:
        if i.isnumeric():
            raise ValueError('Plaintext should not include numbers')

    plaintext = utils.strip(plaintext).upper()
    key = utils.strip(key).upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                'X', 'Y', 'Z']
    encrypt = ''
    key_dict = {}
    for i in range(26):
        key_dict[alphabet[i]] = key[i]
    for i in plaintext:
        encrypt += key_dict[i]

    return encrypt


def decrypt(ciphertext, key):
    """
    Function -- decrypt
        implement substitution cipher
    Parameters:
        ciphertext: encrypted data
        key: a variable as part of the algorithm
    Returns the unencrypted data
    """
    if not isinstance(ciphertext, str):
        raise TypeError('Plaintext should be a string')
    if ciphertext == '':
        raise ValueError('Plaintext can not be empty')
    if not isinstance(key, str):
        raise TypeError('Key should be a string')
    if len(key) != 26:
        raise ValueError('Key should be at the length of 26')
    for i in ciphertext:
        if i.isnumeric():
            raise ValueError('Plaintext should not include numbers')
    key = utils.strip(key).upper()
    decrypt = ''
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                'X', 'Y', 'Z']
    key_dict = {}
    for i in range(26):
        key_dict[key[i]] = alphabet[i]

    for i in ciphertext:
        decrypt += key_dict[i]
    return decrypt
