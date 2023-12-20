import math
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
    whiteball_count = int(input('How many white balls would you like to draw from for the 5 winning numbers?: '))
    redball_count = int(input('How many red balls would you like to draw from for the 2 winning numbers?: '))
    maxred = 69
    maxwhite = 26
    totalmax = maxred+maxwhite
    newmax = whiteball_count+redball_count
    whiteodds = math.factorial(whiteball_count)/(math.factorial(5)*math.factorial(whiteball_count-5))
    redodds = math.factorial(redball_count)/(math.factorial(1)*math.factorial(redball_count-1))
    totalodds = whiteodds * redodds
    print('\nYou have a 1 in ', totalodds,'chance of winning this lottery.  Good luck!')

    break