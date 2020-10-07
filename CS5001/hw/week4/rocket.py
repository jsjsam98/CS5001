'''
Shangjun Jinag
CS 5001, Fall 2020
HW 4 -- Rocket
'''

pattern_string = '\n'


def head():
    global height
    global pattern_string
    i = 1
    half_width_head = 2*height-1
    while i <= half_width_head:
        line = ' '*abs(i-half_width_head-1)+'/'*i+'**'+'\\'*i
        pattern_string += line+'\n'
        # print(line)  # if dont need print, please annotate this line
        i += 1


def head_end():
    global height
    global pattern_string
    i = 1
    half_width_head = 2*height-1
    while i <= half_width_head:
        line = ' '*abs(i-half_width_head-1)+'/'*i+'**'+'\\'*i
        if i < half_width_head:
            pattern_string += line+'\n'
        else:
            pattern_string += line
        # print(line)  # if dont need print, please annotate this line
        i += 1


def cut_body():
    global height
    global pattern_string
    line = '+'+'=*'*height*2+'+'
    pattern_string += line+'\n'
    # print(line)  # if dont need print, please annotate this line


def body_1():
    global height
    global pattern_string
    i = 1
    while i <= height:
        line = '|'+'.'*(i-1)+'\\/'*(height-i+1)+'.'*(i-1) * \
            2+'\\/'*(height-i+1)+'.'*(i-1)+'|'
        pattern_string += line+'\n'
        # print(line)  # if dont need print, please annotate this line
        i += 1
    while i <= 2*height:
        line = '|'+'.'*(2*height-i)+'/\\'*(i-height)+'.' * \
            (2*height-i)*2+'/\\'*(i-height)+'.'*(2*height-i)+'|'
        pattern_string += line+'\n'
        # print(line)  # if dont need print, please annotate this line
        i += 1


def body_2():
    global height
    global pattern_string
    i = 1
    while i <= height:
        line = '|'+'.'*(height-i)+'/\\'*(i)+'.' * \
            (height-i)*2+'/\\'*(i)+'.'*(height-i)+'|'
        pattern_string += line+'\n'
        # print(line)  # if dont need print, please annotate this line
        i += 1
    while i <= 2*height:
        line = '|'+'.'*(i-height-1)+'\\/'*(2*height-i+1)+'.'*(i-height-1) * \
            2+'\\/'*(2*height-i+1)+'.'*(i-height-1)+'|'
        pattern_string += line+'\n'
        # print(line)  # if dont need print, please annotate this line
        i += 1


def main():
    global height
    global pattern_string
    height = int(input('Enter size: '))

    if height < 3:
        print('Rocket sizes must be at least 3')
    else:
        head()
        cut_body()
        body_1()
        cut_body()
        body_2()
        cut_body()
        body_1()
        cut_body()
        head_end()
    print(pattern_string)  # if dont need print, please annotate this line
    return(pattern_string)


if __name__ == '__main__':
    main()
