def distance(value, from_units, to_units):

    if from_units == 'cm':
        c_value = value/100
    elif from_units == 'm':
        c_value = value
    elif from_units == 'km':
        c_value = value/0.001
    elif from_units == 'in':
        c_value = value/39.370078740157
    elif from_units == 'ft':
        c_value = value/3.2808398950131
    elif from_units == 'yd':
        c_value = value/1.0936132983377
    elif from_units == 'mi':
        c_value = value/0.00062137119223733
    else:
        print('ERROR: cannot convert {} {} to {}'.format(
            value, from_units, to_units))
        return float(-1)

    if to_units == 'cm':
        c_value = c_value*100
    elif to_units == 'm':
        c_value = c_value
    elif to_units == 'km':
        c_value = c_value*0.001
    elif to_units == 'in':
        c_value = c_value*39.370078740157
    elif to_units == 'ft':
        c_value = c_value*3.2808398950131
    elif to_units == 'yd':
        c_value = c_value*1.0936132983377
    elif to_units == 'mi':
        c_value = c_value*0.00062137119223733
    else:
        print('ERROR: cannot convert {} {} to {}'.format(
            value, from_units, to_units))
        return float(-1)

    print(value, from_units, 'is equal to', c_value, to_units)
    return c_value


def volume(value, from_units, to_units):

    if from_units == 'l':
        c_value = value
    elif from_units == 'cup':
        c_value = value/4.2267528377
    elif from_units == 'qt':
        c_value = value/1.0566882094
    elif from_units == 'gal':
        c_value = value/0.2641720524
    else:
        print('ERROR: cannot convert {} {} to {}'.format(
            value, from_units, to_units))
        return float(-1)

    if to_units == 'l':
        c_value = c_value
    elif to_units == 'cup':
        c_value = c_value*4.2267528377
    elif to_units == 'qt':
        c_value = c_value*1.0566882094
    elif to_units == 'gal':
        c_value = c_value*0.2641720524
    else:
        print('ERROR: cannot convert {} {} to {}'.format(
            value, from_units, to_units))
        return float(-1)

    print(value, from_units, 'is equal to', c_value, to_units)
    return c_value


def weight(value, from_units, to_units):

    if from_units == 'lb':
        c_value = value
    elif from_units == 'oz':
        c_value = value/16
    elif from_units == 'ton':
        c_value = value/0.0005
    elif from_units == 'gr':
        c_value = value/453.59237
    elif from_units == 'kg':
        c_value = value/0.45359237
    elif from_units == 'st':
        c_value = value/0.0714285714
    else:
        print('ERROR: cannot convert {} {} to {}'.format(
            value, from_units, to_units))
        return float(-1)

    if to_units == 'lb':
        c_value = c_value
    elif to_units == 'oz':
        c_value = c_value*16
    elif to_units == 'ton':
        c_value = c_value*0.0005
    elif to_units == 'gr':
        c_value = c_value*453.59237
    elif to_units == 'kg':
        c_value = c_value*0.45359237
    elif to_units == 'st':
        c_value = c_value*0.0714285714
    else:
        print('ERROR: cannot convert {} {} to {}'.format(
            value, from_units, to_units))
        return float(-1)

    print(value, from_units, 'is equal to', c_value, to_units)
    return c_value


def temperature(value, from_units, to_units):

    if from_units == to_units:
        c_value = value
    else:
        if from_units == 'F' and to_units == 'C':
            c_value = (value-32)*(5/9)
        elif from_units == 'C' and to_units == 'F':
            c_value = value*(9/5)+32
        else:
            print('ERROR: cannot convert {} {} to {}'.format(
                value, from_units, to_units))
            return float(-1)
    print(value, from_units, 'is equal to', c_value, to_units)
    return c_value


def main():
    print('What type of unit would you like to convert:\n'
          '1 - distance    (cm, m, km, in, ft, yd, mi)\n'
          '2 - temperature (C, F)\n'
          '3 - volume      (l, cup, qt, gal)\n'
          '4 - weight      (oz, lb, ton, gr, kg, st)')
    choice = input('Enter choice: \n')

    if choice == '1':
        value = float(input('Enter value to convert: '))
        from_units = str(input('Enter units to convert from: '))
        to_units = str(input('Enter units to convert to: \n'))
        distance(value, from_units, to_units)
    elif choice == '2':
        value = float(input('Enter value to convert: '))
        from_units = str(input('Enter units to convert from: '))
        to_units = str(input('Enter units to convert to: \n'))
        temperature(value, from_units, to_units)
    elif choice == '3':
        value = float(input('Enter value to convert: '))
        from_units = str(input('Enter units to convert from: '))
        to_units = str(input('Enter units to convert to: \n'))
        volume(value, from_units, to_units)
    elif choice == '4':
        value = float(input('Enter value to convert: '))
        from_units = str(input('Enter units to convert from: '))
        to_units = str(input('Enter units to convert to: \n'))
        weight(value, from_units, to_units)
    else:
        print('INVALID CHOICE')


if __name__ == '__main__':
    main()
