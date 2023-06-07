#Nested if else statements

our_list = [3]
our_string = "Yes"

if our_list:
    print('This has something in it.')
else:
    print('NADA.')

if our_string:
    print('There is something here.')
else:
    print('Nope on a roap.')

print('--------------------BREAK-------------------')

teams = ['knicks','bulls','nuggets','kings','heat', 'celtics','pacers']
teams.sort(reverse = True)
for team in teams:
    if team.startswith('n'):
        print(f'The {team.title()} could win the NBA championship this year!')
        if team == 'nuggets':
            print(f'I know {team.title()} will win!')
        else:
            print('They probably wont win though...')
    elif team.startswith('p'):
        print(f'The {team.title()} will probably make the playoffs.')
        if team == 'pacers':
            print('They really need Reggie Miller back.')
    else:
        print(f'The {team.title()} stand no chance this year.')
