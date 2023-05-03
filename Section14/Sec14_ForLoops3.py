#List slicing

numbers = list(range(1,11))
for num in numbers:
    print(num)

print('\n slicing!')
# for num in numbers[0:5]:
for num in numbers[5:]:
    print(num)

new_numbers = numbers
print(new_numbers)
print(type(new_numbers))
#left here on 02.05.2023

# numbers.pop()
# print(numbers)
# print(new_numbers)

new_numbers = numbers[:]
print(new_numbers)
numbers.pop()
print(numbers)
print(new_numbers)