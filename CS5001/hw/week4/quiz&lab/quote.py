list_total = []


def read_sentence():
    length = int(input('Enter length: '))
    i = 0
    list_sentence = []
    while i < length:
        x = input('< ')
        list_sentence.append(x)
        i += 1
    global list_total
    list_total.append(list_sentence)


def repeat_read():
    times = int(input('Number of sentences: '))
    i = 0
    while i < times:
        read_sentence()
        i += 1


def list_print(content):
    x = len(content)
    print('> ', end='')
    for i in range(0, x-1):
        print(content[i], end=' ')
    print(content[x-1], end='.')


def main():
    repeat_read()
    i = 0
    x = len(list_total)
    print('Quote:')
    while i < x:
        list_print(list_total[i])
        print()
        i += 1


if __name__ == '__main__':
    main()
