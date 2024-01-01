print('Sec39_PythonDice.py app')

# How many sides would you like on your dice: 
# How many dice would you like to roll:
# You rolled 5, 6-sided dice.
# Results are as follows: 2,5,4,6,1
# The total value of your roll is 18
# Would you like to roll again?
import math
import random

def dice_sides():
    '''Ask how many sides to a die'''
    sides = int(input('How many sides would you like per die?:  '))
    return sides

def dice_qty():
    '''Ask how many dice to roll'''
    qty = int(input('How many dice would you like to roll?:  '))
    return qty

def rolled_dice(sides,qty):
    '''Sim rolling dice'''
    dice = []
    print('We are going to roll',qty,',',sides,'-sided dice!')
    print('\n-------Results are as follows-------')
    for i in range(qty):
        value = random.randint(1,sides)
        print(f"\t{str(value)})")
        dice.append(value)
    return dice

def sum_dice(dice):
    '''Add all values of dice to a list'''
    print(f"The total value of your roll is {str(sum(dice))}.")
    # Using our own method
    total = 0
    for die in dice:
        total += die
    print(f"The total value of your roll is {str(total)}.")
    return total
def roll_again():
    '''Ask to roll again'''
    choice = input('\nWould you like to roll again??: (y/n) ').lower().strip()
    if choice != 'y':
        roll = False
    else:
        roll = True
    return roll

print('Welcome to the python dice app!')
rolling = True
while rolling:
    # Get info from user
    d_sides = dice_sides()
    d_qty = dice_qty()

    my_dice = rolled_dice(d_sides, d_qty)
    my_sum = sum_dice(my_dice)
    rolling = roll_again()
print('Thank you for using the python dice app!')