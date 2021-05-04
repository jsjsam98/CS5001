import os
filename = '123.txt'

if not os.path.exists(filename):
    raise FileNotFoundError('{} does not exist'.format(filename))
print('xxxxxxxxxxx')
file = open(filename)