import utils


def encrypt(plaintext, alpha_key, numeric_key, adder_key):
    """
    Function -- encrypt
        implement straddle cipher
    Parameters:
        plaintext: unencrypted data
        key: a variable as part of the algorithm
    Returns the encrypted data
    """
    if not isinstance(plaintext, str):
        raise TypeError('Plaintext should be a string')
    if not isinstance(alpha_key, str):
        raise TypeError('Alpha_key should be a string')
    if plaintext == '':
        raise ValueError('Plaintext can not be empty')
    if len(str(numeric_key)) != 2:
        raise ValueError('Numeric_key should be at the length of 2')
    if len(alpha_key) != 26:
        raise ValueError('Key should be at the length of 26')
    for i in plaintext:
        if i.isnumeric():
            raise ValueError('Plaintext should not include numbers')

    plaintext = utils.strip(plaintext).upper()
    alpha_key = utils.strip(alpha_key).upper()
    position1 = str(numeric_key)[0]
    position2 = str(numeric_key)[1]
    key_list = list(alpha_key)
    numeric_key = str(numeric_key)
    adder_key = str(adder_key)
    encrypt_dict = {}
    encrypt_dict['0'] = position2 + '8'
    encrypt_dict['1'] = position2 + '9'
    ini_encrypt = ''  # the initial numeric text

    for index in range(0, 10):
        if index != int(position1) and index != int(position2):
            encrypt_dict[key_list.pop(0)] = str(index)
    for index in range(0, 10):
        encrypt_dict[key_list.pop(0)] = str(position1) + str(index)
    for index in range(0, 8):
        encrypt_dict[key_list.pop(0)] = str(position2) + str(index)

    for i in plaintext:
        ini_encrypt += encrypt_dict[i]

    # prepare for decrypt the adder_text
    decrypt_dict = {}
    decrypt_dict[position2 + '8'] = '0'
    decrypt_dict[position2 + '9'] = '1'
    key_list = list(alpha_key)
    for index in range(0, 10):
        if index != int(position1) and index != int(position2):
            decrypt_dict[str(index)] = key_list.pop(0)
    for index in range(0, 10):
        decrypt_dict[str(position1) + str(index)] = key_list.pop(0)
    for index in range(0, 8):
        decrypt_dict[str(position2) + str(index)] = key_list.pop(0)

    # non-carry addition to the initial numeric text
    done = False
    index = 0
    count = 0
    encrypt = ''
    adder_text = ''
    while not done:
        non_carry = int(ini_encrypt[index]) + int(adder_key[count])
        if non_carry >= 10:
            non_carry = str(non_carry)[1]
        else:
            non_carry = str(non_carry)
        adder_text += non_carry
        index += 1
        count += 1
        if count == len(adder_key):
            count = 0
        if index == len(ini_encrypt):
            done = True

    # decrypt the adder_text
    index = 0
    done = False
    if adder_text[-1] == position1 or position2:
        adder_text = adder_text[:-1]

    while not done:
        if int(adder_text[index]) != int(position1) and\
                int(adder_text[index]) != int(position2):

            encrypt += decrypt_dict[adder_text[index]]
            index += 1
        else:
            encrypt += decrypt_dict[adder_text[index]+adder_text[index + 1]]
            index += 2
        if index >= len(adder_text):
            done = True

    return encrypt


def decrypt(ciphertext, alpha_key, numeric_key, adder_key):
    """
    Function -- decrypt
        implement substitution cipher
    Parameters:
        plaintext: encrypted data
        key: a variable as part of the algorithm
    Returns the unencrypted data
    """
    if not isinstance(ciphertext, str):
        raise TypeError('Ciphertext should be a string')
    if not isinstance(alpha_key, str):
        raise TypeError('Alpha_key should be a string')
    if ciphertext == '':
        raise ValueError('Ciphertext can not be empty')
    if len(str(numeric_key)) != 2:
        raise ValueError('Numeric_key should be at the length of 2')
    if len(alpha_key) != 26:
        raise ValueError('Key should be at the length of 26')
    position1 = str(numeric_key)[0]
    position2 = str(numeric_key)[1]
    key_list = list(alpha_key)
    numeric_key = str(numeric_key)
    adder_key = str(adder_key)
    # from numeric to alpha
    decrypt_dict = {}
    decrypt_dict[position2 + '8'] = '0'
    decrypt_dict[position2 + '9'] = '1'
    for index in range(0, 10):
        if index != int(position1) and index != int(position2):
            decrypt_dict[str(index)] = key_list.pop(0)
    for index in range(0, 10):
        decrypt_dict[str(position1) + str(index)] = key_list.pop(0)
    for index in range(0, 8):
        decrypt_dict[str(position2) + str(index)] = key_list.pop(0)

    # from alpha to numeric
    encrypt_dict = {}
    encrypt_dict['0'] = position2 + '8'
    encrypt_dict['1'] = position2 + '9'
    key_list = list(alpha_key)
    ini_encrypt = ''  # the initial numeric text
    for index in range(0, 10):
        if index != int(position1) and index != int(position2):
            encrypt_dict[key_list.pop(0)] = str(index)
    for index in range(0, 10):
        encrypt_dict[key_list.pop(0)] = str(position1) + str(index)
    for index in range(0, 8):
        encrypt_dict[key_list.pop(0)] = str(position2) + str(index)

    for i in ciphertext:
        ini_encrypt += encrypt_dict[i]

    done = False
    index = 0
    count = 0
    decrypt = ''
    num_text = ''

    while not done:
        if int(ini_encrypt[index]) >= int(adder_key[count]):
            ini = int(ini_encrypt[index]) - int(adder_key[count])
            num_text += str(ini)

        else:
            ini = int(ini_encrypt[index]) + 10 - int(adder_key[count])
            num_text += str(ini)
        index += 1
        count += 1
        if count == len(adder_key):
            count = 0
        if index == len(ini_encrypt):
            done = True
    done = False
    index = 0
    while not done:
        if int(num_text[index]) != int(position1) and\
                int(num_text[index]) != int(position2):
            decrypt += decrypt_dict[num_text[index]]
            index += 1
        else:
            if index < len(num_text)-1:
                decrypt += decrypt_dict[num_text[index] + num_text[index + 1]]
                index += 2
            else:
                index += 1  # may lose some elements
        if index >= len(num_text):
            done = True
    return decrypt
