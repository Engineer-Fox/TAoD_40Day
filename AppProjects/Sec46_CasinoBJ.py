#  Blackjack App
#  Table min $20
# How much money willing to play
# Deal 2 cards
# Hit or stay

class Card():
    def __init__(self,rank,value,suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def displayCard(self):
        '''Show the rank and suit of the card dealt'''
        print(self.rank + ' of '+self.suit)

class Deck():
    pass

class Player():
    pass

class Dealer():
    pass

class Game():
    pass

