text=['abcdefg','hijklmn','opq','rst','uvwxyz']
# line one is used for test
for i in text:
    if len(i) >= 4:
        print(i[0:4])
    else:
        print()
