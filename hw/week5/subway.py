'''
Shangjun Jiang
CS 5001, Fall 2020
HW 5 -- subway

This is a subway guideline program
'''


def is_valid_station(name):
    '''
    Function -- is_valid _station
        decide whether name is a valid station
    Parameters:
        name -- name of station
    Returns True if it is valid
    '''
    if name in station_total:
        return True
    else:
        return False


def on_redline(name):
    '''
    Function -- on_redline
        decide whether name is on redline
    Parameters:
        name -- name of station
    Returns True if it is
    '''
    if name in red:
        return True
    else:
        return False


def on_orangeline(name):
    '''
    Function -- on_orangeline
        decide whether name is on orangeline
    Parameters:
        name -- name of station
    Returns True if it is
    '''
    if name in orange:
        return True
    else:
        return False


def on_blueline(name):
    '''
    Function -- on_blueline
        decide whether name is on blueline
    Parameters:
        name -- name of station
    Returns True if it is
    '''
    if name in blue:
        return True
    else:
        return False


def on_greenline(name):
    '''
    Function -- on_greenline
        decide whether name is on greenline
    Parameters:
        name -- name of station
    Returns True if it is
    '''
    if name in green:
        return True
    else:
        return False


def get_intersecting_station(line_one, line_two):
    '''
    Function -- get_intersecting_station
        get the intersect of line_one and line_two
    Parameters:
        line_one -- name of line, first letter dapitalized
        line_two -- name of line, first letter dapitalized
    Returns name of the intersect station
    '''
    name_list = ['Orange', 'Blue', 'Green', 'Red']
    if line_one in name_list and line_two in name_list:
        line_one_list = eval(line_one.lower())
        line_two_list = eval(line_two.lower())
        intersect = list(set(line_one_list) & set(line_two_list))
        if intersect == []:
            return None
        else:
            return intersect[0]
    else:
        return None


def get_line(name):
    '''
    Function -- get_line
        get the line of the station, if it is an intersect station,
        return orange in priority
    Parameters:
        name -- name of station
    Returns the list of station of a line
    '''
    if name in orange:
        line = orange
    elif name in blue:
        line = blue
    elif name in red:
        line = red
    elif name in green:
        line = green
    else:
        return None
    return line


def get_same_line(station1, station2):
    '''
    Function -- get_same_line
        if two stations are in same line, get the line name
    Parameters:
        station1 -- name of station
        station2 -- name of station
    Returns the name of line of the two station
            otherwise return None
    '''
    if ((station1 in orange) and (station2 in orange)):
        return 'Orange'
    elif ((station1 in green) and (station2 in green)):
        return 'Green'
    elif ((station1 in blue) and (station2 in blue)):
        return 'Blue'
    elif ((station1 in red) and (station2 in red)):
        return 'Red'
    else:
        return False


def get_line_name(name):
    '''
    Function -- get_line_name
        get the name of line, not the list
        return orange in priority
    Parameters:
        name -- name of station
    Returns the name of the line
    '''
    if name in orange:
        line_name_string = 'Orange'
    elif name in blue:
        line_name_string = 'Blue'
    elif name in green:
        line_name_string = 'Green'
    elif name in red:
        line_name_string = 'Red'
    else:
        return None
    return line_name_string


def get_direction(start, end):
    '''
    Function -- get_direction
        get the direction from start to end if they are in same line
    Parameters:
        start -- name of station
        end -- name of station
    Returns the last station of the direction
    '''
    line_name = []
    if ((start in green) & (end in green)):
        line_name = green
    elif((start in blue) & (end in blue)):
        line_name = blue
    elif((start in orange) & (end in orange)):
        line_name = orange
    elif((start in red) & (end in red)):
        line_name = red
    else:
        return None
    start_num = line_name.index(start)
    end_num = line_name.index(end)
    if end_num > start_num:
        return line_name[-1]
    elif end_num < start_num:
        return line_name[0]
    else:
        return None


def get_number_stops(start, end):
    '''
    Function -- get_number_stops
        count the stops between two station in a same line
    Parameters:
        start -- name of station
        end -- name of station
    Returns the number of stops needed
    '''
    line_name = []
    if ((start in green) & (end in green)):
        line_name = green
    elif((start in blue) & (end in blue)):
        line_name = blue
    elif((start in orange) & (end in orange)):
        line_name = orange
    elif((start in red) & (end in red)):
        line_name = red
    else:
        return -1
    start_num = line_name.index(start)
    end_num = line_name.index(end)
    return abs(start_num-end_num)


def duplicate_change(name):
    '''
    Function -- duplicate_change
        change the duplicate name into the same station
    Parameters:
        nmae -- name of station
    Returns the number of station in abbreviation
    '''
    if name == 'Kendall':
        name = 'MIT'
    elif name == 'Charles':
        name = 'MGH'
    elif name == 'Umass':
        name = 'JFK'
    return name


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


def main():

    msg = ''
    start = input('Enter starting station: ')
    end = input('Enter destination station: ')
    start = duplicate_change(start)
    end = duplicate_change(end)
    if is_valid_station(start) and is_valid_station(end):
        pass
    else:
        print("I've never heard of that station, please try again")
        return

    start_line = get_line(start)
    end_line = get_line(end)

    # if the two stations are in the same line
    if get_same_line(start, end) is not False:
        direction = get_direction(start, end)
        step = get_number_stops(start, end)
        case = 1  # go to destination directly

    # two different lines but one in orange
    elif ((end_line == orange) or (start_line == orange)):
        intersect = get_intersecting_station(
            get_line_name(start), get_line_name(end))
        direction1 = get_direction(start, intersect)
        direction2 = get_direction(intersect, end)
        step1 = get_number_stops(start, intersect)
        step2 = get_number_stops(intersect, end)
        step = step1+step2
        case = 2  # go to destination through two lines

    # two different lines and neither in orange
    else:
        intersect1 = get_intersecting_station(
            get_line_name(start), 'Orange')
        intersect2 = get_intersecting_station(
            get_line_name(intersect1), get_line_name(end))
        direction1 = get_direction(start, intersect1)
        direction2 = get_direction(intersect1, intersect2)
        direction3 = get_direction(intersect2, end)
        step1 = get_number_stops(start, intersect1)
        step2 = get_number_stops(intersect1, intersect2)
        step3 = get_number_stops(intersect2, end)
        step = step1+step2+step3
        case = 3  # go to destination through three lines

    if case == 1:
        if step == 1:
            s_num = 0
        else:
            s_num = 1
        start_line_name = get_same_line(start, end)
        msg += 'Get on the {} Line at {} towards {}'.format(
            start_line_name, start, direction)+'\n'
        msg += 'Take the train for {} stop{} and arrive at {}'.format(
            step, 's'*s_num, end)
        print(msg)

    elif case == 2:
        if step1 == 1:
            s_num1 = 0
        else:
            s_num1 = 1
        if step2 == 1:
            s_num2 = 0
        else:
            s_num2 = 1
        start_line = get_line_name(start)
        intersect_line = get_same_line(intersect, end)
        msg += 'Get on the {} Line at {} towards {}'.format(
            start_line, start, direction1)+'\n'
        msg += 'Take the train for {} stop{} and arrive at {}'.format(
            step1, 's'*s_num1, intersect)+'\n'
        msg += 'Get on the {} Line at {} towards {}'.format(
            intersect_line, intersect, direction2)+'\n'
        msg += 'Take the train for {} stop{} and arrive at {}'.format(
            step2, 's'*s_num2, end)
        print(msg)

    elif case == 3:
        if step1 == 1:
            s_num1 = 0
        else:
            s_num1 = 1
        if step2 == 1:
            s_num2 = 0
        else:
            s_num2 = 1
        if step3 == 1:
            s_num3 = 0
        else:
            s_num3 = 1
        start_line = get_line_name(start)
        intersect1_line = get_line_name(intersect1)
        intersect2_line = get_same_line(intersect2, end)
        msg += 'Get on the {} Line at {} towards {}'.format(
            start_line, start, direction1)+'\n'
        msg += 'Take the train for {} stop{} and arrive at {}'.format(
            step1, 's'*s_num1, intersect1)+'\n'
        msg += 'Get on the {} Line at {} towards {}'.format(
            intersect1_line, intersect1, direction2)+'\n'
        msg += 'Take the train for {} stop{} and arrive at {}'.format(
            step2, 's'*s_num2, intersect2)+'\n'
        msg += 'Get on the {} Line at {} towards {}'.format(
            intersect2_line, intersect2, direction3)+'\n'
        msg += 'Take the train for {} stop{} and arrive at {}'.format(
            step3, 's'*s_num3, end)
        print(msg)
    else:
        print("I can't help you with that one!")


if __name__ == '__main__':
    main()
