words = {'computer': 'an electronic device for storing and porcessing data.',
         'data': 'facts and statistics collected together for reference or analysis',
         'science': 'the intellectual and practical activity',
         'exam': 'short for examination'}

for k, v in words.items():
    if k[0] != 'e':
        print('{0} -- {1}'.format(k, v))
