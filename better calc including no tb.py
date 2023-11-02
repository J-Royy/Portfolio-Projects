def start_calc():
    try:
        num1 = float(input('Enter first number!: '))
        op = input('Enter an operator! (+,-,* or /): ')
        num2 = float(input('Enter second number!: '))
        if op == '+':
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print('Wrong operator! Try again!')
            start_calc()
    except:
            print('Error occurred.. Try again!: ')
            start_calc()

start_calc()



