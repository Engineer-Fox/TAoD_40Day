#Looping througha numerical range

# values = range(1,16)

# print(values)
# print(type(values))

# for i in values:
#     print(i)

# for num in range(5):
#     print(num)

# for i in range(2,22,2):
#     print(i)

# for i in range(0,51,3):
#     print(i)
# print('ALL DONE!')

# word = 'Hello World!'
# list_word = list(word)
# print(word)
# print(list_word)
# print(len(list_word))

# list_word[5] = "NEW"
# print(list_word)

# new_word = ' '.join(list_word)
# print(new_word)

numbers = list(range(10,101,10))
# print(numbers)

for n in numbers:
    print(n)
print('\n \n')

squares = []

for num in numbers:
    square = num**2
    squares.append(square)
    # could add, print(square), here to print each square after each loop is complete
    # instead of adding a separate for loop with print statement
print('Populating complete!\n')
for square in squares:
    print(square)