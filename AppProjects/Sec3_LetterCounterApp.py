Welcome = 'Welcome to the Letter Counter App!'

print(Welcome)

name = input('What is your name?: ')
print(f'Hello, {name}!')

print('I will count the number of times that a specific letter occurs in a message!')

message = input('Please enter a message of your choice. : ')
print(message)

letter_of_choice = input('Which letter would you like to count the occurences of?: ')
print(f'Thank you for picking {letter_of_choice}, {name}!  I will tell you how many times it appears!')

#remember the METHOD .count !!!!! 
letter_count = message.count(letter_of_choice)
print(f'The letter {letter_of_choice} appeared {letter_count} times!')

word_of_choice = input('Please enter the word you would like to search for: ')

word_count = message.count(word_of_choice)
print(f'The word "{word_of_choice}", appeared {word_count} times!')
