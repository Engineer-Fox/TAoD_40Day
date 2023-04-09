name = 'Dalton'
age = 32
money = 1.1

#print using string concatenation
print(name + ' is ' + str(age) + ' and has $' + str(money) + ' million, in the bank!')

#print using the .format()
print("{0} is {1} and has ${2} million in the bank!".format(name, age, money))

# print using f-strings
print(f'{name} is {age} and has ${money} million in the bank!')
