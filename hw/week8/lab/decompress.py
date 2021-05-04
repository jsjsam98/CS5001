'''
Northeastern University - Khoury College of Computer Science
CS5001 Online Fall 2020 Jump
Module 9 Lab -- Recursion
Name: Shangjun Jiang

Starter file -- For this lab we are providing students with this file to start
their implementation of the lab.  This file contains the following (in order):

find_end -- a helper function (read documentation for what it does)
decompress -- this is the function shell that the student should implement
main -- a main function that is written to test the student's decompress.
   The main function already has the provided exampled encoded into it.
   The student should add their own test cases in the student examples
   section. For full credit, each test should test a different configuration.
'''


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

    result = ""
    i = 0
    while i < len(original):
        if original[i].isdigit():
            times = int(original[i])

            while original[i+1].isdigit():
                times = 10*times+int(original[i+1])
                i += 1

            start = i + 1
            last = find_end(original, start, level)
            sub = original[start + 1:last]
            result += times * decompress(sub, level)
            i = last
        else:
            result += original[i]
        i += 1
    return result


def main():
    passed = True
    ORIGINAL = 0
    EXPECTED = 1
    # The test cases that were provided as examples in the description
    provided = [
        ("3[b]", "bbb"),
        ("3[b3[a]]", "baaabaaabaaa"),
        ("3[b2[ca]]", "bcacabcacabcaca"),
        ("5[a3[b]1[ab]]", "abbbababbbababbbababbbababbbab"),
    ]
    # Run the provided tests cases
    for t in provided:
        actual = decompress(t[ORIGINAL], 0)
        if actual != t[EXPECTED]:
            print("Error decompressing:", t[ORIGINAL])
            print("   Expected:", t[EXPECTED])
            print("   Actual:  ", actual)
            print()
            passed = False

    # TODO: Add your original tests using the same syntax as above
    student = [
        ("3[awd]", "awdawdawd"),
        ("3[w1[b3[a]]]", "wbaaawbaaawbaaa"),
        ("3[[a]]", "[a][a][a]"),
        ("13[a]", "aaaaaaaaaaaaa"),
        ("20[c]", "cccccccccccccccccccc"),
    ]
    # Run the student test cases
    for t in student:
        actual = decompress(t[ORIGINAL], 0)
        if actual != t[EXPECTED]:
            print("Error decompressing:", t[ORIGINAL])
            print("   Expected:", t[EXPECTED])
            print("   Actual:  ", actual)
            print()
            passed = False

    # print that all the tests passed
    if passed:
        print("All tests passed")


if __name__ == '__main__':
    main()
