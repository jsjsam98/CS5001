''' Align Online CS5001
    Module: Dictionaries & Sets
    Example of using a dictionary to implement a phone book
'''

contacts = {}


def add(name, number):
    ''' Function: add -- adds a name into the phone book
                         if it doesn't already exist
        Params:   name -- the name to add (key)
                  number -- the associated number to add (value)
        Returns True if the name was successfully added, false otherwise
    '''
    if name in contacts:
        return False
    else:
        contacts[name] = number
        return True


def lookup(name):
    ''' Function: lookup -- looks up a name in our phone book
        Params:   name -- the name to look up
        Returns the associated phone number
    '''
    if name in contacts:
        return contacts[name]
    else:
        return "not found"


def update(name, number):
    ''' Function: update -- updates the value associated with a name 
                            in the phone book
        Params:   name -- the name to update
                  number -- the new associated number
        Returns True if the entry was successfully updated, false otherwise
    '''
    if name in contacts:
        contacts[name] = number
        return True
    else:
        return False


def remove(name):
    ''' Function: remove -- removes an entry from the phone book
        Params:   name -- the key value to remove
        Returns True if the name was successfuly removed, false otherwise
    '''
    if name in contacts:
        del contacts[name]
        return True
    else:
        return False


def get_choice():
    ''' Function: get_choice -- menu of options for the program
        Params:   none
        Returns the choice from the menu
    '''
    choices = ("A", "L", "U", "R", "Q")
    print("A -- Add a new contact")
    print("L -- Look-up an existing contact")
    print("U -- Update an existing contact")
    print("R -- Remove an existing contact")
    print("Q -- quit")
    choice = input("Enter choice: ")
    choice = choice.upper()
    while choice not in choices:
        choice = input("Invalid choice, try again: ")
        choice = choice.upper()
    print()
    return choice


def main():
    ''' Function: main -- the main program
        Params:   none
        Returns nothing
    '''
    while True:
        choice = get_choice()
        if choice == "Q":
            break

        elif choice == "A":
            name = input("Enter name: ")
            number = input("Enter number: ")
            if add(name, number):
                print(name, "added")
            else:
                print(name, "is already in the phone book")

        elif choice == "L":
            name = input("Enter name: ")
            number = lookup(name)
            print(name, ":", number)

        elif choice == "U":
            name = input("Enter name: ")
            number = input("Enter new number: ")
            if update(name, number):
                print(name, "updated")
            else:
                print(name, "is not in the phone book")

        elif choice == "R":
            name = input("Enter name: ")
            if remove(name):
                print(name, "removed")
            else:
                print(name, "is not in the phone book")

        else:
            print("Error: should never get here: ", choice)

        print()


if __name__ == "__main__":
    main()
