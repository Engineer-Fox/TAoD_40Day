import math
import random
print('This is the Sec37_PowerBallSim app!')

print('-------------------------------------- Power-Ball Simulator ----------------------------------------')
# How many white balls to draw from
# How many red balls to draw from
# You have a 1 in xxx chance of winning this lottery
# purchase tickets in what interval?

# ------Welcome to Power-Ball ------
# Tonight's winning numbers are x number chosen combining red and white ball total

powering = True
while powering:
    whiteball_count = int(input('How many white balls would you like to draw from for the 5 winning numbers? (Normally there are 69): '))
    if whiteball_count <5:
        whiteball_count = 5
    redball_count = int(input('How many red balls would you like to draw from for the 2 winning numbers? (Normally there are 26): '))
    if redball_count <2:
        redball_count = 2
    maxred = 69
    maxwhite = 26
    totalmax = maxred+maxwhite
    newmax = whiteball_count+redball_count
    whiteodds = math.factorial(whiteball_count)/(math.factorial(5)*math.factorial(whiteball_count-5))
    redodds = math.factorial(redball_count)/(math.factorial(1)*math.factorial(redball_count-1))
    totalodds = whiteodds * redodds
    print('\nYou have a 1 in ', totalodds,'chance of winning this lottery.  Good luck!')

    break
# Get ticket interval
ticketInterval = int(input('Puchase tickets in what interval?:  '))
winningwhite_numbers = []
while len(winningwhite_numbers)<5:
    number = random.randint(1, whiteball_count)
    if number not in winningwhite_numbers:
        winningwhite_numbers.append(number)

winningred_numbers = []
while len(winningred_numbers)<2:
    number = random.randint(1, redball_count)
    if number not in winningred_numbers:
        winningred_numbers.append(number)
winning_numbers = winningred_numbers + winningwhite_numbers
winning_numbers.sort()
# winning_numbers= winning_numbers.append(winningwhite_numbers)
# winning_numbers.sort()
print(winning_numbers)

# Starting to track tickets purchased and winning tickets
boughttickets = 0
keepbuying = True
soldtickets = []
# set while loop to track winning numbers in tickets sold
while winning_numbers not in soldtickets and keepbuying == True:
    lottery_numbers = []
    while len(lottery_numbers)<5:
        number = random.randint(1, whiteball_count)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    lottery_numbers.sort()
    number = random.randint(1,redball_count)
    lottery_numbers.append(number)
    # This currenty ticket has not been sold
    if lottery_numbers not in soldtickets:
        boughttickets += 1
        soldtickets.append(lottery_numbers)
        print(lottery_numbers)
    else:
        print('Losing ticket generated; disregard...')
    
    if boughttickets % ticketInterval == 0:
        print(str(boughttickets), 'tickets purchased so far with no winners...')
        choice = input('\nKeep purchasing tickets?: (Y/N)').lower().strip()
        if choice != 'y':
            keepbuying = False
if lottery_numbers == winning_numbers:
    print('\nWinning ticket numbers:  ', end='')
    for number in lottery_numbers:
        print(str(number),end='')
    print('\nPurchased a total of',str(boughttickets),' tickets.')
else:
    print('\nYou bought ', str(boughttickets),' tickets.')
    print('Better luck next time!')
