def main():
    first = input('Please enter the first time: ')
    second = input('Please enter the second time: ')
    hour1 = int(first[0:2])
    minute1 = int(first[2:4])
    hour2 = int(second[0:2])
    minute2 = int(second[2:4])

    if minute2-minute1 >= 0:
        hour_final = hour2-hour1
        minute_final = minute2-minute1
    else:
        hour_final = hour2-hour1-1
        minute_final = 60+minute2-minute1

    print('{} hours {} minutes'.format(hour_final, minute_final))


if __name__ == '__main__':
    main()
