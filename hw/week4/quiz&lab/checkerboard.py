def checkerboard(width, height):
    '''
    Function checkerboard reads two int representing its width and height
    Return a checkerboard consists of 'o' and 'x'
    '''
    pattern_str = ''
    i = 1  # width variable
    j = 1  # height variable
    while j <= height:
        i = 1

        if j % 2 == 1:
            while i <= width:
                if i % 2 == 1:
                    pattern_str += ('X')
                else:
                    pattern_str += ('O')
                i += 1

        else:
            while i <= width:
                if i % 2 == 1:
                    pattern_str += ('O')
                else:
                    pattern_str += ('X')
                i += 1
        # print('')
        pattern_str += '\n'
        j += 1
    print(pattern_str)
    return pattern_str


def main():

    width = int(input('Please enter the width of checkerboard: \n'))
    height = int(input('Please enter the height of checkerboard: \n'))
    checkerboard(width, height)


if __name__ == '__main__':
    main()
