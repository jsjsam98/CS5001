def arrowhead(size):
    '''
        This function reads an int to represent the arrow size
        It return a arrowhead-like string with 2*size-1 lines
    '''
    def count(mid):
        '''
            This function is help to simplify the program
            receive an int number mid
            return list 1 to mid to 1. e.g. count(5)=[1,2,3,4,5,4,3,2,1]
        '''
        list_num = []
        for k in range(0, 2*mid-1):
            if k < mid:
                list_num.append(k+1)
            else:
                list_num.append(2*mid-k-1)
        return list_num

    pattern_str = ''
    list_num = count(size)
    i = 0
    while i < 2*size-1:
        list_num = count(size)
        pattern_str += '*'*list_num[i]+'\n'
        i += 1
    print(pattern_str)  # if dont need print, user can annotate this line
    return pattern_str


def main():
    size = int(input('Enter the size of the arrowhead: \n'))
    arrowhead(size)


if __name__ == '__main__':
    main()
