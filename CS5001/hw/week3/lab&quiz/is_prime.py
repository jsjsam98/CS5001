def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return 'It is not a prime number'
            break
        i = i+1
        if i == num:
            return 'It is a prime number'


def main():
    num = float(input('Give me a number: '))
    text = is_prime(num)
    print(text)


if __name__ == '__main__':
    main()
