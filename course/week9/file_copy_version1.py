"""
Module: Handing Exceptions

This file implements copying the poems file
"""


def main():
    input = open("poems.txt")
    content = input.read()
    input.close()

    print(content)

    output = open("poems-copy.txt", "w")
    output.write(content)
    output.close()


main()
