'''
Shangjun Jiang
CS 5001, Fall 2020
HW 5 -- subway_test

This is a test program
'''
from subway import *
red = ['Alewife', 'Davis', 'Porter', 'Harvard',
       'Central', 'MIT', 'MGH', 'Downtown Crossing',
       'South Station', 'Broadway', 'Andrew', 'JFK']
orange = ['Oak Grove', 'Malden Center', 'Wellington',
          'Assembly', 'Sullivan Square', 'Community College',
          'North Station', 'Haymarket', 'State', 'Downtown Crossing',
          'Chinatown', 'Tufts Medical Center', 'Back Bay', 'Mass Avenue',
          'Ruggles', 'Roxbury Crossing', 'Jackson Square',
          'Stony Brook', 'Green Street', 'Forest Hills']
blue = ['Wonderland', 'Revere Beach', 'Beachmont', 'Suffolk Downs',
        'Orient Heights', 'Wood Island', 'Airport', 'Maverick',
        'Aquarium', 'State']
green = ['Haymarket', 'Government Center',
         'Park Street', 'Boylston', 'Arlington', 'Copley',
         'Haynes Convention Center', 'Kenmore',
         'Blandford Street', 'Boston University East',
         'Boston University Central', 'Boston University West',
         'Saint Paul Street', 'Pleasant Street', 'Babcock Street',
         'Packards Corner', 'Harvard Avenue', 'Griggs Street',
         'Allston Street', 'Warren Street', 'Washington Street',
         'Sutherland Road', 'Chiswick Road', 'Chestnut Hill Avenue',
         'South Street', 'Boston College']
#  Kendall/Mit, Charles/MGh, Umass/JFK
duplicate_name = ['Kendall', 'Charles', 'UMass']
station_total = red+orange+blue+green+duplicate_name


def test_is_valid_station(ini_input, result):
    outcome = is_valid_station(ini_input)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_on_redline(ini_input, result):
    outcome = on_redline(ini_input)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_get_intersecting_station(line_one, line_two, result):
    outcome = get_intersecting_station(line_one, line_two)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_get_same_line(station1, station2, result):
    outcome = get_same_line(station1, station2)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_get_direction(station1, station2, result):
    outcome = get_direction(station1, station2)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def test_get_number_stops(station1, station2, result):
    outcome = get_number_stops(station1, station2)
    if outcome == result:
        print('Pass!')
    else:
        print('Fail!')


def main():

    #  test for is_valid_station
    print('...start testing is_valid_station')
    test_is_valid_station('Revere Beach', True)
    test_is_valid_station('Wrong Name', False)

    #  test for on_redline
    print('...start testing on_redline')
    test_on_redline('Central', True)
    test_on_redline('Wrong Name', False)

    #  test for get_intersecting_station
    print('...start testing get_intersecting_station')
    test_get_intersecting_station('Orange', 'Blue', 'State')
    test_get_intersecting_station('Wrong Name', 'Orange', None)

    #  test for get_same_line
    print('...start testing get_same_line')
    test_get_same_line('Allston Street', 'Washington Street', 'Green')
    test_get_same_line('Wrong Name', 'Roxbury Crossing', False)

    #  get_line and get_line_name return list and string respectively,
    #  which are not precise and return 'orange' if it is an intersect

    #  test for get_direction
    print('...start testing get_direction')
    test_get_direction('Allston Street', 'Washington Street', 'Boston College')
    test_get_direction('Wrong Name', 'Roxbury Crossing', None)

    #  test for get_number_stops
    print('...start testing get_number_stops')
    test_get_number_stops('North Station', 'Haymarket', 1)
    test_get_number_stops('Wrong Name', 'Roxbury Crossing', -1)


if __name__ == '__main__':
    main()
