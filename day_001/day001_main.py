if __name__ == '__main__':
    print('Welcome to the Band Name Generator')
    city = input('What\'s name of the city you grew up in?\n')
    pet = input('What\'s your pet\'s name?\n')
    band_name =  ' '.join([city, pet])
    print(f'Your band name could be {band_name}')

