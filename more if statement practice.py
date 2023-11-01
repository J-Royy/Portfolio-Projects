
age = int(input('Hello! Confirm your age!: '))
if age >= 18:
    print('Welcome!, Let\'s get you a drink!')
    print('*hands you a menu*')
elif age <= 0:
    print('You weren\'t even born yet..!')
else:
    print('You must be 18 or older to drink! Goodbye!')
    quit()
