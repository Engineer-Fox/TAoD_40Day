#Thesaurus app
import random
print('Welcome to the thesaurus app!')

thesaurus = {
        'happy':['marry','gay','extatic','elated','jovial'],
        'hot':['scorching','sweaty','stifling','boiling','tropical'],
        'cold':['frigid','freezing','cool','polar','chilly'],
        'sad':['morose','unhappy','downtrodden','miserable','glum'],
}

print('Choose a word from the thesaurus and I will give you a synonym!')
print('Here are the words in the thesaurus:')
for key in thesaurus.keys():
    print(f'\t-{key}')
# get user info
choice = input('\nWhat word would you like a synonym for?: ').lower().strip
#provide random synonym
if choice in thesaurus.keys():
    index = random.randint(0,4)
    print(f'A synonym for {choice} is {str(thesaurus[choice])}.')
#Choose a word from the thesaurus and I will give you a synonym
#Here are the words in the thes
#What word would you like a syn for?
#A syn for ___ is merry
#Would you like to see the whole thes? (yes/no):