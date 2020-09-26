from unit_converter import distance
EPSILON = 0.001


def test_distance(value,from_units,to_units, expected):

    print('Testing {} converting from {} to {}'.format(value,from_units,to_units), sep='')
    actual = distance(value,from_units,to_units)
    return abs(actual - expected) < EPSILON

def run_distance_tests():
    ''' function run_distance_tests
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    # Test 1: (0, 0), (0, 0). Expected: 0
    num_fail = 0
    if (test_distance(100,'cm','m',1)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    return num_fail

def main():
    print('Testing distance convert functions...\n\n')
    failures = run_distance_tests()
    if failures == 0:
        print('Everything passed, great job functions!')
    else:
        print('Something went wrong, go back and fix pls.')
    

if __name__ == '__main__':
    main()