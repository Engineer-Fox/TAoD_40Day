print('Welcome to the Fibonacci Calculator App')
import math

comp_in = int(input('How many digits (places) of the Fibonacci Sequence would you like to compute?: '))

fib = [1,1]
for n in range(comp_in-2):
    new_fib = fib[n] + fib[n+1]
    fib.append(new_fib)
print(f'\n The first {str(comp_in)} numbers of the Fibonacci Sequence are: ')
for n in fib:
    print(n)

golden = []
for n in range(len(fib)-1):
    f_ratio = fib[n+1]/fib[n]
    golden.append(f_ratio)

print('The corresponding golden ration is: ')
for f_ratio in golden:
    print(f_ratio)

