'''
Homework 2
Name: Shangjun Jiang
Course number: CS5001
Semester: Fall 2020

'''


import math


def main():
    TC = float(input('Enter total cost of purchase: '))
    AP = float(input('Enter amount paid: '))
    change = round((AP-TC), 2)

    if change < 0:
        print('Did not receive enough cash from the customer.')

    else:
        cInt = math.floor(change)
        cFra = round((change-cInt)*100)
        twenties = cInt//20
        tens = (cInt % 20)//10
        fives = (cInt % 10)//5
        ones = cInt % 5
        quarters = (cFra//25)
        dimes = ((cFra % 25)//10)
        nickels = (((cFra % 25) % 10)//5)
        pennies = (cFra % 5)

        print('Change to be given:  {}'.format(change))

        if twenties > 0:
            if twenties == 1:
                Ntwenties = 'twenty'
            else:
                Ntwenties = 'twenties'

            print('{} {}'.format(twenties, Ntwenties))

        if tens > 0:
            if tens == 1:
                Ntens = 'ten'
            else:
                Ntens = 'tens'

            print('{} {}'.format(tens, Ntens))

        if fives > 0:
            if fives == 1:
                Nfives = 'five'
            else:
                Nfives = 'fives'

            print('{} {}'.format(fives, Nfives))

        if ones > 0:
            if ones == 1:
                Nones = 'one'
            else:
                Nones = 'ones'

            print('{} {}'.format(ones, Nones))

        if quarters > 0:
            if quarters == 1:
                Nquarters = 'quarter'
            else:
                Nquarters = 'quarters'

            print('{} {}'.format(quarters, Nquarters))

        if dimes > 0:
            if dimes == 1:
                Ndimes = 'dime'
            else:
                Ndimes = 'dimes'

            print('{} {}'.format(dimes, Ndimes))

        if nickels > 0:
            if nickels == 1:
                Nnickels = 'nickel'
            else:
                Nnickels = 'nickels'

            print('{} {}'.format(nickels, Nnickels))

        if pennies > 0:
            if pennies == 1:
                Npennies = 'penny'
            else:
                Npennies = 'pennies'

            print('{} {}'.format(pennies, Npennies))


if __name__ == '__main__':
    main()
