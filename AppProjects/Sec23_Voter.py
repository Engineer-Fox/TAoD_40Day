print('Welcome to the Voter Registration App!')

name = (input('What is your name?:  ').title())
age = int(input('What is your age?:  '))

if name == '':
    print('PLEASE ENTER YOUR NAME!')
else:
    print(f'Hello, {name}!  Welcome to the app!')

if age <= 18:
    print('You are not old enough!')
else:
    print('Congratulations!  You are old enough to vote!')

parties = ['Republican', 'Democratic','Independent','Libertarian','Green']

print('Here is a list of political parties to join:')
for n in parties:
    print(f'- {n}')

choice = (input('Which party would you like to join?:  ').title().strip())
print(f'Congratulations {name}!  You have joined the {choice} party!')

if choice == 'Republican':
    print('This is a major party of the United States.')
elif choice == 'Democratic':
    print('This is a major party of the United States.')
elif choice == 'Independent':
    print("This isn't really a party, as much as an abstention from a party...")
else:
    print('This is not a major party, and you will probably not have any impact on the results of the elections...')