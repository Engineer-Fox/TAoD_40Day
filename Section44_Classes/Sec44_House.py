# Another look at classes

class House():
    '''A class to model a house that is for sale.'''

    def __init__(self, style, sqft, yearbuilt,price):
        pass
        self.style = style
        self.sqft = sqft
        self.yearbuilt = yearbuilt
        self.price = price

        self.sold = False
        self.weeks_on_market = 0
    
    def display_info(self):
        '''Display info on the house'''
        print('\n-----------House for sale---------')
        print('House Style:\t'+self.style)
        print('Square Footage:\t'+str(self.sqft))
        print('Year Built:\t'+str(self.yearbuilt))
        print('Sale Price:\t'+str(self.price)) 
        print('\nThis house have been on the market for '+str(self.weeks_on_market)+' weeks.')

    def sell_house(self):
        '''Sell the house!!'''
        if self.sold == False:
            print('Congratulations!  Your house has been sold for $:'+str(self.price)+'!')
            self.sold = True
        else:
            print('Sorry, this house in no longer for sale.')

    def change_price(self,amount):
        '''Change the sale price of the house'''
        self.price += amount
        if amount < 0:
            print('Price drop!!! Holy shit!!!')
        else:
            print('The house has increase in value by $'+str(amount)+'.')
    def update_weeks(self):
        '''Increment the number of weeks a house has been on the market.'''
        self.weeks_on_market += 1

my_house = House('Ranch', 3200, 1979, 450000)

print(my_house.style)
print(my_house.sqft)
print(my_house.price)
print(my_house.sold)
my_house.display_info()