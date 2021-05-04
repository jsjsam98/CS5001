filename = 'college.txt'
input_file = open(filename, 'r')
filedata = input_file.readlines()

content = ''
for i in filedata:

    i = i.strip().lower()
    content += i+'\t'
content_list = content.split()

# add a comma in the mark list
mark = [':', ';', '.', '?', '!', ',']
word_dict = {}
count = 0
for i in content_list:
    if i[-1] in mark:
        i = i[0:-1]
    if i[-1] == '-':
        i = content_list[count][0:-1] + content_list[count + 1]
        del content_list[count + 1]
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

    count += 1
print(word_dict)