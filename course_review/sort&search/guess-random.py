''' Align Online CS5001
    Module 14 -- Efficiency
    Sample code -- implementation of a guessing game that just makes randome guesses
'''
import random


class Guessing_game:
    ''' Class that represents a random guessing game. '''

    def __init__(self, num_range):
        # the range of numbers we are guessing
        self.range = num_range
        # the values we have guessed so far
        self.guessed = []

    def next_guess(self, dir):
        '''
        Method: next_guess -- guess the next number
        Parameter:
           self -- the current object
           dir -- the direction the next guess should be
        Returns the next guess to make
        '''
        found = False
        while not found:
            if dir == "l":
                # guess a number between 1 and the previous guess
                guess = random.randint(1, self.prev_guess - 1)
            elif dir == "h":
                # guess a number between the previous guess and the highest number
                guess = random.randint(self.prev_guess + 1, self.range)
            else:
                # game just started so we just pick a random number
                guess = random.randint(1, self.range)
            # have we guessed this before?
            if not (guess in self.guessed):
                found = True
        # new guess needs to be saved and returned
        self.prev_guess = guess
        self.guessed.append(guess)
        return guess


def main():
    '''
    Function: main -- the driver program
    '''
    # instantiates the guessing game class
    game = Guessing_game(100)
    # keep track of how many guesses have been made
    count = 0
    guessed = False
    dir = ""
    print("Think of a mystery number between 1 and 100")
    while not guessed:
        # what is your next guess
        guess = game.next_guess(dir)
        count += 1
        # displays the computer's guess
        print("The computer guesses", guess, "; ", end="")
        # get information from us to see if the computer is right
        dir = input("correct, lower or higher (c, l, h)? ")
        if dir == "c":
            guessed = True
    print("I needed", count, "guesses--I hope that's good!")


if __name__ == "__main__":
    main()
