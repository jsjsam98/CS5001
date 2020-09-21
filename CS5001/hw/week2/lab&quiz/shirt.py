def main():
    temp = int(input('Enter temperature: '))
    if temp > 90:
        print('tanktop')
    elif temp <= 90 and temp > 70:
        print('short-sleeve shirt')
    elif temp <= 70 and temp > 50:
        print('long-sleeve shirt')
    elif temp <= 50 and temp > 32:
        print('sweater')
    else:
        print('stay in bed')


if __name__ == '__main__':
    main()
