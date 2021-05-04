def make_palindrome(s):
    if len(s) == 0:
        return ""
    result = ""
    result += s[0]
    result += make_palindrome(s[1:])
    result += s[0]
    return result
