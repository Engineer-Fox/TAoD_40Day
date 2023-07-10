#simple if else statements

colors = ['red', 'green', 'yellow', 'blue']
for color in colors:
    print(color)

for color in colors:
    if color == 'red':
        print(color.upper())
        print(f'I love {color.upper()} whenever I see it!')
    else:
        print(f'{color.upper()} was NOT found!  BITCH!')

age = int(input("What's my age again?: "))
if age >= 21:
    print()
    print('Have yourself a LEGAL drink!')
else:
    print(age)
    print('No drinky-poo for you!')

first = input('\nWhat is your first name?: ')
last = input('\nWhat is your last name?: ')

if first == 'John' and last == 'Fox':
    print('What a swell guy.')
else:
    print('Ewwwwwwww.')
