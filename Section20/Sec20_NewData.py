#boolean values of true or false

status = True
print(status)
print(type(status))
print('BREAK')

soda = 'coke'
print(soda == 'coke')
print(soda == 'pepsi')
print(soda != 'root beer')
print('BREAK')

names = ['mike', 'john','dave','pete']
mike_status = 'mike' in names
bill_status = 'bill' in names
print(mike_status)
print(bill_status)
print('BREAK')

peter_status = 'peter' not in names
print(peter_status)