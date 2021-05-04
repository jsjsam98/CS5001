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
duplicate_name = ['Kendall', 'Charles', 'UMass']
station_total = red+orange+blue+green+duplicate_name

def get_direction(start, end):
    '''return the first or the last station in the whole line
       if start, end are not in the same line, return None
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

def main():
  
    a=get_direction('Malden Center','Malden Cneter')
    print(a)

if __name__ == '__main__':
    main()