'''Python Calculator App'''

# Enter two numbers and an operation and the desired operation will be performed
# Enter a number
# Enter another number
# Operator (addition, subtraction, mult, divi, expo):
# The ___ of x and y is z.
# Would you like to run the program again? y/n
# negatives and positives
# for mult
def add(a,b):
    '''Addition operation'''
    summation = round(a+b, 4) 
    print('The sum of',a,'and',b,'is',summation,'!')
    return str(a)+"+"+str(b)+'='+str(summation)+"."
def subtract(a,b):
    '''Subtraction'''
    difference = round(a-b, 4)
    print('The difference of',a,'and',b,'is',difference,'!')
    return str(a)+"-"+str(b)+'='+str(difference)+"."
def multi(a,b):
    '''Mult'''
    product = round(a*b,4)
    print('The product of',a,'and',b,'is',product,'!')
    return str(a)+"*"+str(b)+'='+str(product)+"."
    
def divi(a,b):
    '''divide'''
    if b != 0:
        quotient = round(a/b,4)
        print('The quotient of',a,'and',b,'is',quotient,'!')
        return str(a)+"/"+str(b)+'='+str(quotient)+"."
    else:
        print('You cant divide by zero dumbass!')
        return 'Div ERROR'
    
def expo(a,b):
    '''Expo'''
    exponentiation = round(a**b,4)
    print('The exponentiation of',a,'and',b,'is',exponentiation,'!')
    return str(a)+"^"+str(b)+'='+str(exponentiation)+"."
print('Welcome to the python calc app! \n Please enter two numbers and the desired operation!')
history = []


running = True
while running:
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number:  '))
    operation = input('What operation would you like? (add, subtract, multiply, divide, exponet)OR(a,s,m,d,e):  ')

    if operation == "add"or operation == 'a':
            result = add(num1,num2)
    elif operation == 'subtract' or operation == 's':
            result = subtract(num1,num2)
    elif operation == 'multiply' or operation == 'm':
        result = multi(num1,num2)
    elif operation == 'divide' or operation == 'd':
            result = divi(num1,num2)
    elif operation == 'exponent' or operation == 'e':
            result = expo(num1,num2)
    else:
        print('That is not a valid operation.')
        result = 'OPP ERROR'
    history.append(result)
    choice = input('Would you like to run the app again?: y/n:  ').lower().strip()
    running = True
    if choice != 'y':
        print('\nCalculation History:')
        for calc in history:
            print(calc)
        print('\nThank you for using the py calc app!')
        running = False
