def histogram():
    '''
        This function returns a histogram of the input numbers in sequence
    '''
    list_hist = []
    done = False
    i = 0
    print('Enter values between 1-50:')
    while not done:
        x = int(input('< '))
        if (x < 1 and x != -1) or x > 50:
            print('Invalid')

        elif x == -1:
            j = 0
            print('Histogram:')
            while j < len(list_hist):
                print('*'*list_hist[j])
                j += 1
            done = True
        else:
            list_hist.append(x)
            i += 1


def main():
    histogram()


if __name__ == '__main__':
    main()
