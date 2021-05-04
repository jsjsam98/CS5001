file = open('book.txt')
content = file.read()
file.close()
book = content.split()
for i in range(len(book)):
    for j in range(len(book[i])):
        if not book[i][j].isalpha():
            k = list(book[i])
            k[j] = ' '
            book[i] = ''.join(k)
    book[i] = book[i].strip().upper()
book_keys = list()
book_dict = {}
for i in book:
    if i != '':
        book_keys.append(i)
for i in range(len(book_keys)):
    if book_keys[i][0] not in book_dict.keys():
        book_dict[book_keys[i][0]] = []
        book_dict[book_keys[i][0]].append(book_keys[i])
    else:
        book_dict[book_keys[i][0]].append(book_keys[i])

print(len(book_dict.keys()))
