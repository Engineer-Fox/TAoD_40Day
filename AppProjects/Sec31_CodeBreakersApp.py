import string
import collections
print('Welcome to the Code Breakers App!')
# import string
# d = dict.fromkeys(string.ascii_lowercase, 0)
# print(d)
# # Alternative way to include numbers and characters in a dict
# punctuation = string.punctuation
# numbers = string.digits
# print(numbers)
# print(punctuation)

non_chars = string.punctuation + string.digits
# key_phrase_1 = input('Enter a word or phrase to count the frequency of occurence of each letter: ').lower().strip()
key_phrase_1 = """
Is this the Region, this the Soil, the Clime,
Said then the lost Arch-Angel, this the seat
That we must change for Heav'n, this mournful gloom
For that celestial light?   Be it so, since he
Who now is Sovran can dispose and bid
What shall be right: fardest from him his best
Whom reason hath equald, force hath made supream
Above his equals.   Farewel happy Fields
Where Joy for ever dwells: Hail horrours, hail
Infernal world, and thou profoundest Hell
Receive thy new Possessor:   One who brings
A mind not to be chang'd by Place or Time.
The mind is its own place, and in it self
Can make a Heav'n of Hell, a Hell of Heav'n.
What matter where, if I be still the same,
And what I should be, all but less then he
Whom Thunder hath made greater? Here at least
We shall be free; th' Almighty hath not built
Here for his envy, will not drive us hence:
Here we may reign secure, and in my choyce
To reign is worth ambition though in Hell:
Better to reign in Hell, then serve in Heav'n.
But wherefore let we then our faithful friends,
Th' associates and copartners of our loss
Lye thus astonisht on th' oblivious Pool,
And call them not to share with us their part
In this unhappy Mansion, or once more
With rallied Arms to try what may be yet
Regaind in Heav'n, or what more lost in Hell?"""
key_phrase_1 = key_phrase_1.lower().strip().replace(' ','')
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
# key_phrase_2 = input('\n\n\nEnter a word or phrase to count the frequency of occurence of each letter: ').lower().strip()
key_phrase_2 = """
That glory never shall his wrath or might
Extort from me. To bow and sue for grace
With suppliant knee, and deify12 his power
Who, from the terror of this arm, so late
Doubted his empire--that were low indeed;
115 That were an ignominy and shame beneath
This downfall; since, by fate, the strength of Gods,
And this empyreal13 substance, cannot fail;
Since, through experience of this great event,
In arms not worse, in foresight much advanced,
120 We may with more successful hope resolve
To wage by force or guile eternal war,
Irreconcilable to our grand Foe,
Who now triumphs, and in th' excess of joy
Sole reigning holds the tyranny of Heaven."""
key_phrase_2 = key_phrase_2.lower().strip().replace(' ','')
for items in non_chars:
    key_phrase_2 = key_phrase_2.replace(items,'')
# Total frequency count to be used from percentage
total_freq = len(key_phrase_2)
letter_count = collections.Counter(key_phrase_2)

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

choice = input('\n\nWould you like to encode or decode a message?: ')
phrase = input('What message would you like to use? ').lower().replace(" ", "")

# Removing all non-letters
for items in non_chars:
    phrase = phrase.replace(items,'')
# Proceeding based on choice made by user
# User wants to encode a message
if choice == 'encode':
    encoded_phrase = []
    for letter in phrase:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)

    print('\nThe encoded message is: ')
    for letter in encoded_phrase:
        print(letter, end='')
# User wants to decode a message
elif choice == 'decode':
    decoded_phrase = []
    for letter in phrase:
        index = key_phrase_2_ordered_letters.index(letter)
        letter = key_phrase_1_ordered_letters[index]
        decoded_phrase.append(letter)
    print('\nThe decoded message is:  ')
    for letter in decoded_phrase:
        print(letter, end='')

            
else:
    print("I'm sorry that is not an option for this program.  Please enter either 'encode' or 'decode'")

