import cmath
print('Welcome to the Quadratic Equation App!\n')

print('\n A quadratic equation is of the form ax^2 + bx + c = 0')
print('Your solutions can be real or complex numbers.')
print('A complex number has two parts: a + bj')
print('\n Where a, is the real portion and bj, is the imaginary portion.')

quant_eq = int(input('How many equations would you like to solve today?: '))

for n in range(quant_eq):
    print(f'\n Solving for equation #{str(n+1)}')
    print('----------------------------      -------------------------')
    a = float(input('Please enter value of a:     (this is the coefficient of x^2)'))
    b = float(input('Please enter value of b:     (this is the coefficient of x)'))
    c = float(input('Please enter value of c:     (this is the coefficient)'))
    #The best way to code using an external library is to import the whole lib and use a . method to call the method/function
    x1 = (-b +cmath.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b -cmath.sqrt(b**2-4*a*c))/(2*a)
    print(f'\n The solutions to {str(a)}x^2 + {str(b)}x + c = 0 are: ')
    print(f'\n tx1 = {str(x1)}')
    print(f'\n tx2 = {str(x2)}')