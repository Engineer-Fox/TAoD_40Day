print('Welcome to Sec36, the guess the word application and work!\n')
# create dict to hold the words
import random
wordchoice_dict = {
    "sports":['basketball', 'football','baseball','waterpolo','volleyball','basketball','hockey','gymnastics','tennis','curling'],
    "colors":['red','yellow','pink','brown','blue','black','white','green','purple','orange'],
    'fruits':['orange','banana','apple','watermellon','peach','mango','grape','berry'],
    'courses':['math','literature','english','physics','biology','thermo','art','fitness']
}
# Create a list of keys
wordchoice_keys = []
for key in wordchoice_dict.keys():
    wordchoice_keys.append(key)

# Control while loop key for playing the game
playing = True
# while loop for the category selection
while playing:
    # need a random key or category
    category = wordchoice_keys[random.randint(0,len(wordchoice_keys)-1)]
    # need a random word from the dict
    word = wordchoice_dict[category] [random.randint(0,len(wordchoice_dict[category])-1)]
    # need a blank word to give hints
    blankword=[]
    for letter in word:
        blankword.append('-')
    # hint statement
    print('Guess a ', str(len(word)),' letter word from the following category: ',category)
    guess = ''
    guess_count = 0
    # need a single while loop for each round
    while guess != word:
        # get a single guess from the user
        print(''.join(blankword))
        guess = input('Enter your guess:  ').lower().strip()
        guess_count += 1
        # guess check correct
        if guess == word:
            print('Correct!  You guessed the word in ', str(guess_count),'guesses, and you are clearly a genius!')
            break
        elif guess != word and guess_count <= len(word):
            print('Try again dipshit....')
            # need to loop through the letters without repeating a letter revealed to the user
            # Also need to replace the dashes we printed earlier in blankword above
            replacingdash = True
            while replacingdash:
                letter_index = random.randint(0,len(word)-1)
                if blankword[letter_index]=='-':
                    blankword[letter_index] = word[letter_index]
                    replacingdash = False
        elif guess != word and guess_count > len(word):
                print('You really needed that much help?!?!?!?!  You suck at this!')
                break
    keepplaying = input('Would you like to keep playing? (y/n):  ').lower().strip()
    if keepplaying != 'y':
        print('Thank you for playing!  Goodbye!')
        break
    else:
        print('Okay!  Here we go again!')
        continue

