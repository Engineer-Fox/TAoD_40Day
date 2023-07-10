import math
import cmath

print('Welcome to the Factorial App!')

number_in = int(input('What number would you like the factorial of?: '))

print(f'{str(number_in)}! = ', end='')

for n in range(1,number_in):
    print(str(n), end ="*")
    # print(f'{str(number_in)}! = {fact_out}')
print(str(number_in))

fact = math.factorial(number_in)
print('\n Here is the result from the Math Lib: ')
print(f'The factorial of {str(number_in)} is {str(fact)}.')

my_fact = 1

for n in range(1, number_in+1):
    my_fact = my_fact*n
print('\n Here is the result from my own algorithm: ')
print(f'The factorial of {str(number_in)} is {str(my_fact)}.')

if my_fact == fact:
    print('All clear here!  The numbers are matching!')
else:
    print('Hold the phone!  We have an issue!')
