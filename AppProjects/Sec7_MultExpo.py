print('Hello!  Welcome to the multiplication and exponentiation table app!')

name = input('What is your name? :  ')
number_in = float(input('What number would you like to work with? :  '))
math_cool = name + '!  Math is soo cool!'

#multiplication table
print('\n Multiplication Table For ' + str(number_in))
print('\n\t 1.0 * ' + str(number_in) + ' = ' + str(round((1*number_in), 4)))
print('\t 2.0 * ' + str(number_in) + ' = ' + str(round((2*number_in), 4)))
print('\t 3.0 * ' + str(number_in) + ' = ' + str(round((3*number_in), 4)))
print('\t 4.0 * ' + str(number_in) + ' = ' + str(round((4*number_in), 4)))
print('\t 5.0 * ' + str(number_in) + ' = ' + str(round((5*number_in), 4)))
print('\t 6.0 * ' + str(number_in) + ' = ' + str(round((6*number_in), 4)))
print('\t 7.0 * ' + str(number_in) + ' = ' + str(round((7*number_in), 4)))
print('\t 8.0 * ' + str(number_in) + ' = ' + str(round((8*number_in), 4)))
print('\t 9.0 * ' + str(number_in) + ' = ' + str(round((9*number_in), 4)))
print('\t 10.0 * ' + str(number_in) + ' = ' + str(round((10*number_in), 4)))

#exponentiation table
print('\n Exponentiation Table For ' + str(number_in))
print('\n\t 1.0 ** ' + str(number_in) + ' = ' + str(round((1**number_in), 4)))
print('\t 2.0 ** ' + str(number_in) + ' = ' + str(round((2**number_in), 4)))
print('\t 3.0 ** ' + str(number_in) + ' = ' + str(round((3**number_in), 4)))
print('\t 4.0 ** ' + str(number_in) + ' = ' + str(round((4**number_in), 4)))
print('\t 5.0 ** ' + str(number_in) + ' = ' + str(round((5**number_in), 4)))
print('\t 6.0 ** ' + str(number_in) + ' = ' + str(round((6**number_in), 4)))
print('\t 7.0 ** ' + str(number_in) + ' = ' + str(round((7**number_in), 4)))
print('\t 8.0 ** ' + str(number_in) + ' = ' + str(round((8**number_in), 4)))
print('\t 9.0 ** ' + str(number_in) + ' = ' + str(round((9**number_in), 4)))
print('\t 10.0 ** ' + str(number_in) + ' = ' + str(round((10**number_in), 4)))

print(f'\n {math_cool}')
print(f'\t {math_cool.lower()}')
print(f'\t\t {math_cool.upper()}')
print(f'\t\t\t {math_cool.title()}')
