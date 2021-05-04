'''
Shangjun Jiang
CS 5001, Fall 2020
HW 8 -- Ciphers
'''

import string
import caesar
import railfence
import playfair
import beale
import straddle
import substitution


def main():
    try:
        done = False
        while not done:
            choose = input('Do you want to encrypt or decrypt?')
            if choose == 'encrypt':

                encrypt = input('Enter an encrypt method: ')

                if encrypt == 'caesar':
                    plaintext = input('Enter plaintext: ')
                    key = input('Enter key: ')
                    if key.isnumeric():
                        key = int(key)
                    else:
                        raise ValueError('Key should be numeric')
                    output = caesar.encrypt(plaintext, key)

                elif encrypt == 'railfence':
                    plaintext = input('Enter plaintext: ')
                    key = input('Enter key: ')
                    if key.isnumeric():
                        key = int(key)
                    else:
                        raise ValueError('Key should be numeric')
                    output = railfence.encrypt(plaintext, key)
                elif encrypt == 'playfair':
                    plaintext = input('Enter plaintext: ')
                    key = input('Enter key: ')
                    if key.isnumeric():
                        raise ValueError('Key should be a string')
                    output = playfair.encrypt(plaintext, key)
                elif encrypt == 'substitution':
                    plaintext = input('Enter plaintext: ')
                    key = input('Enter key: ')
                    if len(key) != 26 or not isinstance(key, str):
                        raise ValueError(
                            'Key should be a string with 26 letters')
                    output = substitution.encrypt(plaintext, key)
                elif encrypt == 'beale':
                    plaintext = input('Enter plaintext: ')
                    key = input('Enter key: ')
                    seed = input('Enter seed: ')
                    if not isinstance(key, str):
                        raise TypeError('Key should be a string')
                    output = beale.encrypt(plaintext, key, seed)
                elif encrypt == 'straddle':
                    plaintext = input('Enter plaintext: ')
                    alpha_key = input('Enter alpha_key: ')
                    numeric_key = input('Enter numeric_key: ')
                    adder_key = input('Enter adder_key: ')
                done = True

            elif choose == 'decrypt':
                ciphertext = input('Enter ciphertext: ')
                key = input('Enter key: ')
                decrypt = input('Enter a decrypt method: ')
                if decrypt == 'caesar':
                    ciphertext = input('Enter ciphertext: ')
                    key = input('Enter key: ')
                    if key.isnumeric():
                        key = int(key)
                    else:
                        raise ValueError('Key should be numeric')
                    output = caesar.decrypt(ciphertext, key)
                elif decrypt == 'railfence':
                    ciphertext = input('Enter ciphertext: ')
                    key = input('Enter key: ')
                    if key.isnumeric():
                        key = int(key)
                    else:
                        raise ValueError('Key should be numeric')
                    output = railfence.decrypt(ciphertext, key)
                elif decrypt == 'playfair':
                    ciphertext = input('Enter ciphertext: ')
                    key = input('Enter key: ')
                    if key.isnumeric():
                        raise ValueError('Key should be a string')
                    output = playfair.decrypt(ciphertext, key)
                elif decrypt == 'substitution':
                    ciphertext = input('Enter ciphertext: ')
                    key = input('Enter key: ')
                    if len(key) != 26 or not isinstance(key, str):
                        raise ValueError(
                            'Key should be a string with 26 letters')
                    output = substitution.decrypt(plaintext, key)
                elif decrypt == 'beale':
                    ciphertext = input('Enter ciphertext: ')
                    key = input('Enter key: ')
                    if not isinstance(key, str):
                        raise TypeError('Key should be a string')
                    output = beale.decrypt(ciphertext, key)
                elif decrypt == 'straddle':
                    ciphertext = input('Enter ciphertext: ')
                    alpha_key = input('Enter alpha_key: ')
                    numeric_key = input('Enter numeric_key: ')
                    adder_key = input('Enter adder_key: ')
                    output = straddle.decrypt(
                        ciphertext, alpha_key, numeric_key, adder_key)
                done = True

            else:
                print('You should enter "encrypt" or "decrypt"')

        print(output)

    except TypeError:
        print('A TypeError occurred')

    except ValueError:
        print('A ValueError occurred')

    else:
        print('An unknown Error occurred')


if __name__ == "__main__":
    main()
