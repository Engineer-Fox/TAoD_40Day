import datetime
print('Welcome to the Grocery List App!')

date1 = datetime.datetime.now()
time1 = datetime.datetime.now()
print(f'Current Date and Time: {date1.hour}:{date1.minute}, {date1.day}-{date1.month}-{date1.year}')

list = ['Meat','Cheese']
print(f'You currently have {list[0]} and {list[1]}')

list.append(input('Type of food to add to the grocery list: '))
print(f'Here is your grocery list: {list}')

list.append(input('Type of food to add to the grocery list: '))
print(f'Here is your grocery list: {list}')

list.append(input('Type of food to add to the grocery list: '))
print(f'Here is your grocery list: {list}')

list.append(input('Type of food to add to the grocery list: '))
print(f'Here is your grocery list: {list}')
print(f'Your list currently has {len(list)}')
list.remove(input('What food did you just buy?: '))
print(f'Your list now only has: {list}')