def translate(day):
    if day == 'Monday':
        spanish_day = 'lunes'
    elif day == 'Tuesday':
        spanish_day = 'martes'
    elif day == 'Wednesday':
        spanish_day = 'miercoles'
    elif day == 'Thursday':
        spanish_day = 'jueves'
    elif day == 'Friday':
        spanish_day = 'viernes'
    elif day == 'Saturday':
        spanish_day = 'sabado'
    elif day == 'Sunday':
        spanish_day = 'domingo'
    else:
        spanish_day = 'Unknown'
    return spanish_day


def main():
    day = input('Enter the day in English: ')
    newName = translate(day)
    print(newName)


if __name__ == '__main__':
    main()
