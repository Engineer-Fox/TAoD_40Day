import random
print('Welcome to the Coin Toss App!')

print('I will flip a coin a set number of times.')

flip_count = int(input('How many times would you like me to flip the coin?:  '))
choice = input('Would you like to see the result of each flip? Y/N:  ')

samples = [random.randint(1,2) for i in range(flip_count)]

heads = samples.count(1)
tails = samples.count(2)
heads_per = round(samples.count(1)/flip_count*100)
tails_per = round(samples.count(2)/flip_count*100)
for n in samples:
    message = 'Heads' if n == 1 else 'Tails'
    if choice == "Y":
        print(message)
    else:
        pass
else:
    print(f'The Heads count is {heads}/{flip_count} and the Tails count is {tails}/{flip_count}.')
    print(f'That is a percentage of {heads_per} % and a percentage of {tails_per} %.')