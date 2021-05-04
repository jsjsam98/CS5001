def make_palindrome(sequence):

    if len(sequence) == 0:
        return ""
    else:
        msg = "" + sequence[0] + make_palindrome(sequence[1:]) + sequence[0]

    return msg

