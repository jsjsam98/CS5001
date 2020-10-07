from unit_converter import distance
from unit_converter import volume
from unit_converter import weight
from unit_converter import temperature
EPSILON = 0.001


def distance_tests(value, from_units, to_units, expected):

    print('Testing {} converting from {} to {}'.format(
        value, from_units, to_units), sep='')
    actual = distance(value, from_units, to_units)
    if actual == -1:
        return 'invalid'
    else:
        return abs(actual - expected) < EPSILON


def volume_tests(value, from_units, to_units, expected):
    print('Testing {} converting from {} to {}'.format(
        value, from_units, to_units), sep='')
    actual = volume(value, from_units, to_units)
    if actual == -1:
        return 'invalid'
    else:
        return abs(actual - expected) < EPSILON


def weight_tests(value, from_units, to_units, expected):
    print('Testing {} converting from {} to {}'.format(
        value, from_units, to_units), sep='')
    actual = weight(value, from_units, to_units)
    if actual == -1:
        return 'invalid'
    else:
        return abs(actual - expected) < EPSILON


def temperature_tests(value, from_units, to_units, expected):
    print('Testing {} converting from {} to {}'.format(
        value, from_units, to_units), sep='')
    actual = temperature(value, from_units, to_units)
    if actual == -1:
        return 'invalid'
    else:
        return abs(actual - expected) < EPSILON


def run_distance_tests():
    ''' function run_distance_tests
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    num_fail = 0

    # Test 1: (100,'cm','m'). Expected: 1
    if (distance_tests(100, 'cm', 'm', 1)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: (100,'m','km'). Expected: 0.1
    if (distance_tests(100, 'm', 'km', 0.1)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: (100,'km','in'). Expected: 3937007.8740157
    if (distance_tests(100, 'km', 'in', 3937007.8740157)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 4: (100,'ft','yd'). Expected: 333.3333333
    if (distance_tests(100, 'ft', 'yd',  33.3333333)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 5: (100,'mmi','yd'). Expected: 'invalid'
    if (distance_tests(100, 'mmi', 'yd',  'invalid')):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1
    return num_fail


def run_volume_tests():
    ''' function run_volume_tests
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    num_fail = 0

    # Test 1: (10,'l','qt'). Expected: 10.566882094
    if (volume_tests(10, 'l', 'qt', 10.566882094)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: (33,'cup','gal'). Expected: 2.0625000
    if (volume_tests(33, 'cup', 'gal', 2.0625000)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: (33,'km','qt'). Expected: 'invalid'
    if (volume_tests(33, 'km', 'qt', 'invalid')):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    return num_fail


def run_weight_tests():
    ''' function run_distance_tests
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    num_fail = 0

    # Test 1: (16,'oz','lb'). Expected: 1
    if (weight_tests(16, 'oz', 'lb', 1)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: (1,'lb','stone'). Expected: 0.0714285714
    if (weight_tests(1, 'lb', 'stone', 0.0714285714)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: (909,'gr','st'). Expected: 0.1431423
    if (weight_tests(909, 'gr', 'st', 0.1431423)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 4: (100,'gram','kg'). Expected: 'invalid'
    if (weight_tests(100, 'gram', 'kg',  'invalid')):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1
    return num_fail


def run_temperature_tests():
    ''' function run_distance_tests
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    num_fail = 0

    # Test 1: (32,'F','C'). Expected: 0
    if (temperature_tests(32, 'F', 'C', 0)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: (100,'C','F'). Expected: 0.0714285714
    if (temperature_tests(100, 'C', 'F', 212)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: (909,'CC','F'). Expected: 'invalid'
    if (temperature_tests(909, 'CC', 'F', 'invalid')):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    return num_fail


def main():
    print('Testing distance convert functions...\n\n')
    failures = run_distance_tests()+run_volume_tests() + \
        run_weight_tests()+run_temperature_tests()
    if failures == 0:
        print('Everything passed, great job functions!')
    else:
        print('Something went wrong, go back and fix pls.')


if __name__ == '__main__':
    main()
