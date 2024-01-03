'''This is the python3 Bank Deposit and Withdrawl App'''

import math
import random

def get_info():
    print('----------------------Welcome to the First Fox National Bank---------------------------')
    name = input('\nHello, what is your name?:  ').title().strip()
    savings = float(input('\n\tHow much money (USD) would you like to deposit to your new savings account?:  '))
    checking = float(input('\n\tHow much money (USD) would you like to deposit to your new checking account?:  '))

    bank_account = {
        'Name':name,
        'Savings':savings,
        'Checking':checking,
    }
    return bank_account

def make_deposit(bank_account,account,money):
    bank_account[account] += money
    print(f"The ${str(money)} was successfully deposited into {bank_account}'s {account.lower()} account.")

def make_withdrawal(bank_account, account, money):
    if bank_account[account]-money >= 0:
        bank_account[account] -= money
        print(f"The ${str(money)} was successfully withdrawn from {bank_account}'s {account.lower()} account.")
    else:
        print(f"I'm sorry, but {bank_account} does not have sufficient funds for the withdrawal.")
        return 'Balanc ERROR'
    
def display_info(bank_account):
    print('\nCurrent Account Information')
    for key, value in bank_account.items():
        if key == 'Name':
            print('\n\t',key,':',str(value))
        else:
            print('\n\t',key,'$',str(value))


my_account = get_info()

running = True

while running:
    display_info(my_account)
    account_type = input('What account would you like to access?  Checking or Savings:  ').title()
    choice = input('What type of transaction would you like to make?  Deposit or Withdrawal:  ').title()
    amount = float(input('How much money (USD)?:  '))
    
    if account_type == 'Checking' or account_type == 'Savings':
        if choice == 'Deposit':
            make_deposit(my_account, account_type, amount)
        elif choice == 'Withdrawal':
            make_withdrawal(my_account, account_type,amount)
        else:
            print("I'm sorry we cannot do that for you today.")
    else:
        print('You have made an incorrect selection.  Please choose from the two available account types.')
        break
    choice = input('Would you like to make another transaction? y/n:  ')
    if choice != 'y':
        running = False
    else:
        running = True
display_info(my_account)
print('Thank you for banking with us, please come back again soon!')
    

