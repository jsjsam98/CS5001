def create_lyrics(animal, voice):

    print('Old MacDonald had a farm, ee-igh, ee-igh, oh!')
    print('And on that far he had a {}, ee-igh, ee-igh, oh!'.format(animal))
    print('With a {}, {} here and a {}, {} there.'.format(
        voice, voice, voice, voice))
    print('Here a {}, there {}, everywhere a {}, {}.'.format(
        voice, voice, voice, voice))
    print('Old MacDonald had a farm, ee-igh, ee-igh, oh!')


def main():

    create_lyrics('cow', 'moo')
    create_lyrics('dog', 'wow')
    create_lyrics('cat', 'meow')
    create_lyrics('pig', 'hooey')
    create_lyrics('goat', 'baa')


if __name__ == '__main__':
    main()
