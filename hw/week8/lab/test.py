def find_end(original, start, level):
    ''' STUDENTS CAN USE THIS FUNCTION AS IS, NO NEED TO MODIFY
        Function: find_end
           Looks through a string that begins with an opening '[' and
           finds the index of the matching closing ']'.  If the provided
           string does not begin with a '[', end with a ']', or has mismatched
           brackets, this function will raise a ValueError.

        Parameters:
           original -- the original string
           start -- starting index of the [
           level -- the level of recursion that can be used to indent 
              output for debugging purposes

        Returns the index of the matching ']'
    '''
    if original[start] != "[":
        message = "ERROR in find_error, must start with [:", original[start:]
        raise ValueError(message)
    indent = level * "  "
    index = start + 1
    count = 1
    while count != 0 and index < len(original):
        if original[index] == "[":
            count += 1
        elif original[index] == "]":
            count -= 1
        index += 1
    if count != 0:
        message = "ERROR in find_error, mismatched brackets:", original[start:]
        raise ValueError(message)
    return index - 1

def find_start(original):
    index = 0
    for i in original:
        if i == '[':
            return index
        index += 1
    return False
        

def decompress(original, level):
    ''' Function: decompress
           Decompresses the provided string.

        Parameters:
           original -- the string to decompress
           level -- the level of recursion that can be used to indent 
              output for debugging purposes

        Returns the decompressed version of the original string
    '''
    # TODO:  Implement me!!
    
    i = original[0]
    times = 1
    start = find_start(original)
    result = ''

    if find_start(original):
        last = find_end(original,start, 0)
        substring = original[start + 1:last]

        if i.isdigit() == True:
            times = int(i)
            result = times * decompress(substring,0)

        else: 
            return i+decompress(original[1:],0)
    else:
        return original

    return result



test_list = '5[a3[b]1[ab]]'
info = decompress(test_list, 0)
print(info)