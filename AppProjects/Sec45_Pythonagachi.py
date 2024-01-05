'''Pythonagachi app'''

import random
class Creature():
    def __init__(self,name):
        '''Initialize attributes'''
        self.name = name.title()

        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 0
        self.is_sleeping = False
        self.is_alive = True
        
    def eat(self):
        '''Simulate eating. Each time you eat, take one food away from inventory
        and randomly take a value away from hunger.'''
        # first make sure food is available
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1,4)
            print(f'{self.name} just had a yummy meal!')
            print(f'Remaining food: {str(self.food)}')
            print(f'Hunger Level: {str(self.hunger)}')
        else:
            print(f'{self.name} does not have any food!  Better forage for some....')
        # if hunger is less than zero, set to zero
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        '''Play a number guessing game between 0 and 2'''
        value = random.randint(0,2)
        print(f'\n{self.name} wants to play a guessing game!')
        print(f'{self.name} is thinking of a number 0,1, or 2...')
        guess = int(input(f'\nWhat is your guess?!?!?!:  '))
        if guess != value:
            print(f' Wrong!  {self.name} was thinking of {str(value)}.')
            self.boredom -= 1
        else:
            print('That is correct!')
            self.boredom -= 3
        
        if self.boredom < 0:
            self.boredom = 0

        self.hunger += 1


    def sleep(self):
        '''Simulate sleeping. Try to wake up creature when asleep;
        tiredness and boredom will decrease after sleeping.'''
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        self.hunger += 1
        print('Zzzzzz.... Zzzzzz.... Zzzzzz....')
        print(f'{self.name} is sleeping.')
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0
        
    def awake(self):
        '''Simulate trying to wake up and eventually waking up the creature'''
        value = random.randint(0,1)
        # trytowake = int(input(f'Try waking up {self.name}'))
        if value == 0:
            print(f'{self.name} just woke up!')
            self.sleeping = False
            self.tiredness = 0
        else:
            print(self.name+'will not wake up...')
            self.sleep()
        
    def clean(self):
        '''Simulate taking a bath'''
        self.dirtiness = 0
        print(f'{self.name} took a bath and is all clean!')

    def forage(self):
        '''Will increase food attribute, but will increase dirtiness'''
        food_found = random.randint(0,4)
        self.food += food_found

        self.dirtiness += 1
        self.hunger += 1
        self.tiredness += 1

        print(f'{self.name} found {str(food_found)} pieces of food!')

    def showValues(self):
        '''Show current values!'''
        print(f'\nCreature Name: {self.name}')
        print(f'Hunger (0-10):  {str(self.hunger)}')
        print(f'Boredom (0-10):  {str(self.boredom)}')
        print(f'Tiredness (0-10):  {str(self.tiredness)}')
        print(f'Dirtiness (0-10):  {str(self.dirtiness)}')
       
        print(f'\nFood Inventory: {str(self.food)} pieces.')
        if self.is_sleeping:
            print(f'Current Status: Sleeping')
        else:
            print(f'Current Status:  Awake')
        
    def incrementValues(self,diff):
        '''Set difficulty and show values'''
        # Increase the hunger and dirtiness regardless of awake or sleep
        self.hunger += random.randint(0,diff)
        self.dirtiness += random.randint(0,diff)
        # Increase boredom or tiredness if awake
        if self.is_sleeping == False:
            self.boredom += random.randint(0,diff)
            self.tiredness += random.randint(0,diff)
        
    def kill(self):
        '''Check all values are less than 10 that may kill the creature'''
        if self.hunger>=10:
            print(f'{self.name} starved to death...')
            self.is_alive = False
        elif self.dirtiness>=10:
            print(f'{self.name} has suffered an infection and died...')
            self.is_alive = False
        elif self.tiredness>=10:
            self.tiredness = 10
            print(f'{self.name} got too tired, and went into a coma...')
            self.is_sleeping = True
        elif self.boredom>=10:
            self.boredom = 10
            print(f'{self.name} went crazy from boredom and fell asleep.')
            self.is_sleeping = True

def showMenu(creature):
    '''Show options for playing the game with the creature'''
    if creature.is_sleeping:
        choice = input(f'\nEnter 6 to try and wake up {creature.name}: ')
        choice = '6'
        
    else:
        print('Enter (1) to eat.')
        print('Enter (2) to play.')
        print('Enter (3) to sleep.')
        print('Enter (4) to take a bath.')
        print('Enter (5) to forage for food.')
        choice = input('What is your choice???:  ')
    return choice

def call_action(creature, choice):
    '''Giving the player's choice, call appropriate class methods'''
    if choice == '1':
        creature.eat()
    elif choice == '2':
        creature.play()
    elif choice == '3':
        creature.sleep()
    elif choice == '4':
        creature.clean()
    elif choice == '5':
        creature.forage()
    elif choice == '6':
        creature.awake()
    else:
        print('Sorry!  That is not an option! Try again!')
        call_action
    
print('Welcome to the Py Sim App')
difficulty = int(input('Please choose a difficulty between 1 and 5 (1-5):  '))
if difficulty > 5:
    difficulty = 5
elif difficulty < 1:
    difficulty = 1

running = True
while running:
    name = input('What name would you like to give you creature pet?:  ')
    player = Creature(name)
    rounds = 1
    # Game loop simulates rounds
    # Keep looping while the creature is alive
    while player.is_alive:
        print('\n----------------------------------------------------')
        print('Round #'+str(rounds))
        player.showValues
        roundMove = showMenu(player)
        call_action(player,roundMove)

        print(f'Round #{str(rounds)} Summary: ')
        player.showValues()
        input('\nPress (ENTER) to continue.')
        
        player.incrementValues(difficulty)

        player.kill()
        
        rounds+=1
    
    print(f'\n\tR.I.P.')
    print(f'{player.name} survived {str(rounds-1)} round.')
    
    playAgain = input('Do you want to play again?: y/n').lower().strip()
    if playAgain != 'y':
        running = False
        print('Thank you for playing our game!  Cheers.')
    else:
        print(f'\nOkay!  Here we go again!')
    