import random
import utils


def encrypt(plaintext, key, seed):
    """
    Function -- encrypt
        implement beale cipher
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
    if not isinstance(seed, int):
        raise TypeError('Seed should be an int')
    for i in plaintext:
        if i.isnumeric():
            raise ValueError('Plaintext should not include numbers')
    plaintext = utils.strip(plaintext).upper()
    encrypt = ''

    file = open(key)
    content = file.read()
    file.close()
    book = content.split()
    random.seed(seed)
    book_dict = {}

    for i in range(len(book)):
        if book[i][0].upper() not in book_dict.keys():
            book_dict[book[i][0].upper()] = []
            book_dict[book[i][0].upper()].append(i + 1)
        else:
            book_dict[book[i][0].upper()].append(i + 1)
    for i in plaintext:
        codes = book_dict[i]
        length = len(codes)

        num = random.randint(0, length - 1)
        encrypt += str(book_dict[i][num]) + ' '
    encrypt = encrypt[:-1]
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
    file = open(key)
    content = file.read()
    file.close()
    book = content.split()
    decrypt = ''
    cipher_list = ciphertext.split()
    for i in cipher_list:
        decrypt += book[int(i)-1][0]
    decrypt = decrypt.upper()
    return decrypt
