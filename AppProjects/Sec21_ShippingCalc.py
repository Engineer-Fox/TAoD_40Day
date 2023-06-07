print('Welcome to the Shipping Accounts Program!')

users = ['eramom','footea','sportsballer','dfox','daltonf', 'johnf']

username = input('What is your username?:  ').lower().strip()
price = [5.10, 5.00, 4.95, 4.80]

if username in users:
    print(f'\n Hellow {username}. Welcome back to your account!')
    print('Current shipping prices are as follows:')
    print(f'\n Shipping orders 0 to 100: \t\t ${str(price[0])}')
    print(f'\n Shipping orders 100 to 500: \t\t ${str(price[1])}')
    print(f'\n Shipping orders 500 to 1000: \t\t ${str(price[2])}')
    print(f'\n Shipping orders over 1000: \t\t ${str(price[3])}')
    quantity = int(input('\nHow many items would you like to ship?:  '))
    if quantity < 100:
        cost = 5.10
    elif quantity < 500:
        cost = 5.00
    elif quantity < 1000:
        cost = 4.95
    else:
        cost = 4.80

    total_cost = quantity * cost
    bill = round(total_cost, 2)
    print(f'The cost to ship {str(quantity)} it will cost ${str(bill)}.')
    confirmation = input('Would you like to ship? (Please type yes/no): ').title()
    if confirmation != 'Yes':
        print('Okay, we will hold off placing the order until you are ready.')
    else:
        print(f'Alrighty.  Shipping {str(quantity)} items for a total cost of ${str(bill)}.')
else:
    print('Incorrect username.  Please try again.')