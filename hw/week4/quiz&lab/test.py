list_total = [1]
list_sentence = []


def read_sentence():
    length = int(input('Enter length: '))
    i = 0
    global list_sentence
    while i < length:
        x = input()
        list_sentence.append(x)
        i += 1
    global list_total
    list_total.append(list_sentence)
    print('finish')


read_sentence()
print(list_sentence)
print(list_total)
