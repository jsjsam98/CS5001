def main():
    value = input('Enter integer value: ')
    word = input('Enter word: ')
    if ((word == 'one' and value == '1') or
       (word == 'two' and value == '2') or
       (word == 'three' and value == '3') or
       (word == 'four' and value == '4') or
       (word == 'five' and value == '5')):
       		print(value, 'and', word, 'are the same number')
    else:
    		print(value, 'and', word, 'are NOT the same number')


if __name__ == '__main__':
	main()