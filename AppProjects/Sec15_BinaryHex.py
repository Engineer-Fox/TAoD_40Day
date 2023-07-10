print('Welcome to the Binary/Hexidecimal Converter App!')

max_value = int(input('Compute binary and hexidecimal values up to the following decimal number: '))
decimal = list(range(1,max_value+1))
binary = []
hexadecimal = []

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print('Generating lists........\n')
print('..................\n')
print('Completed!')

print('\n Using slicing, we will now show a portion of each list!')

lower_range = int(input('What decimal number would you like to begin with?: '))
upper_range = int(input('What number would you like to end with?: '))

print(f'\n Decimal values from {lower_range} to {upper_range}:')
for num in decimal[lower_range-1:upper_range]:
    print(num)
print(f'\n Binary values from {lower_range} to {upper_range}:')
for num in binary[lower_range-1:upper_range]:
    print(num)
print(f'\n Hexadecimal values from {lower_range} to {upper_range}:')
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)

input(f'\n Press Enter to see all values from 1 to {max_value}.')
print('Decimal-----Binary-----Hexadecimal')
print('-----------------------------------')
for d,b,h in zip(decimal,binary,hexadecimal):
    print(str(d)+'-----'+str(b)+'-----'+str(h))


print('\n The entire list has been output to your screen!')