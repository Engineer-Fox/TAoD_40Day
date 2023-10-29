import string
import collections
print('Welcome to the frequency analysis app!')

# import string
# d = dict.fromkeys(string.ascii_lowercase, 0)
# print(d)
# # Alternative way to include numbers and characters in a dict
# punctuation = string.punctuation
# numbers = string.digits
# print(numbers)
# print(punctuation)

non_chars = string.punctuation + string.digits
key_phrase_1 = input('Enter a word or phrase to count the frequency of occurence of each letter: ').lower().strip()
for items in non_chars:
    key_phrase_1 = key_phrase_1.replace(items,'')
# Total frequency count to be used from percentage
total_freq = len(key_phrase_1)
# instantiating lib collections.method
letter_count = collections.Counter(key_phrase_1)
# 
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_freq
    percentage = round(percentage,2)
    print(f'\t {key}\t {str(value)}\t {str(percentage)}%')
#Making a list of most common letters from highest to lowest.
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])
# Printing that list
print('\nLetters ordered from highest occurence to lowest: ')
for letter in key_phrase_1_ordered_letters:
    print(letter, end='')

## Beginning new input for key phrase 2
key_phrase_2 = input('\n\n\nEnter a word or phrase to count the frequency of occurence of each letter: ').lower().strip()
for items in non_chars:
    key_phrase_2 = key_phrase_2.replace(items,'')
# Total frequency count to be used from percentage
total_freq = len(key_phrase_2)
letter_count = collections.Counter(key_phrase_2)
# 
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_freq
    percentage = round(percentage,2)
    print(f'\t {key}\t {str(value)}\t {str(percentage)}%')
#Making a list of most common letters from highest to lowest.
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_2_ordered_letters.append(pair[0])
# Printing that list
print('\nLetters ordered from highest occurence to lowest: ')
for letter in key_phrase_2_ordered_letters:
    print(letter, end='')