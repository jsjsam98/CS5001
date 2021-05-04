"""
Module: Handing Exceptions

This file implements copying the poems file and modifying the lines
"Roses are red" to all upper-case.
"""


def main():
    input = open("poems.txt", "r")
    output = open("poems-copy.txt", "w")

    for line in input:
        if line.strip() == "Roses are red":
            output.write(line.upper())
        else:
            output.write(line)

    input.close()
    output.close()


main()
