first_name=input('Please enter your first name: ')

print('Hello, ' + first_name.title())

number = input('Please enter your favorite number: ')
print(number)
print(type(number))

print(int(number))

print('Give me any two numbers, and I will multiply them together!')
num_1 = int(input('First number: '))
num_2 = int(input('Second number: '))

product_1 = num_1*num_2
print('The product of ' + str(num_1) +' and '+str(num_2) + 'is'+ str(product_1) +'!')
