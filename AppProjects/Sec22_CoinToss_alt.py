import random
print('Welcome to the Coin Toss App!')

print('I will flip a coin a set number of times.')

flip_count = int(input('How many times would you like me to flip the coin?:  '))
choice = input('Would you like to see the result of each flip? Y/N:  ')
print('\nFlipping now!')

heads = 0
tails = 0

for flips in range (flip_count):
    coin = random.randint(0,1)
    if coin == 1:
        heads += 1
        if choice.startswith('y'):
            print('HEADS')
    else:
        tails += 1
        if choice.startswith('y'):
            print('TAILS')

    if heads == tails:
        print(f'At {str(flips + 1)} the number of heads and tails were equal at {str(heads)}.')

heads_per = round(heads/flip_count*100)
tails_per = round(tails/flip_count*100)

print(f'\nResults of randomly flipping the coin out of {str(flip_count)} times.')
print(f'\n\t\t Percentage')
print(f'Heads\t\t{str(heads)}/{str(flip_count)}\t\t{str(heads_per)}%')
print(f'Tails\t\t{str(tails)}/{str(flip_count)}\t\t{str(tails_per)}%')