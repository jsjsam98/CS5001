"""
Module: Handing Exceptions

This file implements the reading of weights from the keyboard
and storing them in a file, one per line
"""
import os


def main():

    try:
        filename = input("Enter filename: ")
        if os.path.isdir(filename):
            prinpt("that is not a file")
        elif os.path.exists(filename):
            answer = input("Do you want to replace the file (y/n): ")
            if answer == "y":
                file = open(filename, "w")
            else:
                file = open(filename, "a")
               number = 0
                while number != -1:
                    try:
                        number = int(input("Enter weight (or -1 to quit): "))
                        if number > 0:
                            file.write(str(number))
                            file.write("\n")

                    except ValueError as ex:
                        print("Enter an integer value.")

                file.close()
    except PermissionError :
        print("You do not have permission to use that file")
    except OSError:
        print("Something happened while writing to the file:", filename)


main()
