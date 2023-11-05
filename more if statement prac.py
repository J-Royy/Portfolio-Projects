KD = float(input('Yo! What\'s your highest K/D ratio in any Call of Duty?: '))

if KD >= float(10):
    print('Whoa, you are godlike!.. are you cheating? xD')
elif KD >= float(5):
    print('You are extremely good!')
elif KD >= float(1.5):
    print('You are above average!')
else:
    print('You could do better!')
