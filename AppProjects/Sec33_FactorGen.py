print('Sec32_FactorGen.py')
print('Welcome to the factor Generator App!')

# Enter a number to determine all factors of that number:
# 100?
# Factors are even quotients or products
# In summary 1 * 100 = 100, 2*50 = 100, 4*25 = 100, 5*20 = 100, 10*10 = 100
flag1=True
flag2=True
# Run the program until the user quits
running=True
while running:
    # Get number from user input
    number = int(input('Enter a number to determine all factors of that number:  '))
    factors=[]
    for i in range (1, number+1):
        if number % i == 0:
            factors.append(i)
    print(f'\nFactors of {str(number)} are:  ')
    for factor in factors:
        print(factor)
    print("\nIn summary:  ")
    for i in range(int(len(factors)/2)):
        print(f'{str(factors[i])} * {factors[-i-1]} = {str(number)}')
    choice = input('Try again? y/n:  ')
    if choice != 'y':
        running = False
        print('Have a great day.')
print('All done!')