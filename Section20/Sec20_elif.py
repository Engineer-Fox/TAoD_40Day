# Elif chains

age = int(input('What is your age?: '))

if age < 18: 
    print(f"You're only {str(age)}!")
    print('You cannot gamble and you cannot drink alcohol!')
elif age < 21:
    print(f'You are only {str(age)}!')
    print('You can play blackjack, but you cannot drink alcohol!')
elif age < 100:
    print(f'Okay good!  You are {str(age)}!')
    print('You can go play some blackjack, and you can have a drink. Cheers!')
 #order of operations, if/elif/else
else:
    print('What the heck are you doing out at a casino?!?!')

print('------------------------- BREAK ------------------------')

num = int(input('What is the number?:  '))

if num < 5:
    print('That is a small number.')

elif num < 10:
    print('That is a smallish number.')

elif num < 15:
    print('That is a medium numbner.')
elif num < 20:
    print('That is a big number.')
elif num <=25:
    print('That is a HUGE number!')
elif num ==40:
    print('I love that number!')
else:
    print('That number is way too big.')
