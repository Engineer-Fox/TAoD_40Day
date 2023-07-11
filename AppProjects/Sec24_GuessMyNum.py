import random
print('Welcome to the Guess My Number App!')

name = (input('Hello!  What is your name?:  ').title().strip())

if bool(name) == True:
    print(f'Well {name}, I am thinking of a number between 1 and 20.')
else:
    print('Please try again, and enter your name.')
    exit()
number = random.randint(1,20)
for guesses in range(4):
    guess = int(input('\nTake a guess:  '))
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    print(f'Good job, {name}!  You guessed my number in {int(guesses + 1)} guesses!')
else:
    print(f'Game Over!  The number I was thinking of was {number}.  Thank you for playing!')
