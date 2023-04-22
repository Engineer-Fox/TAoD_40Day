print('Welcome to the Basketball Roster Program!')

player_roster = []

player = input('Who is your point guard?: ').title()
player_roster.append(player)
player = input('Who is your shooting guard?: ').title()
player_roster.append(player)
player = input('Who is your center?: ').title()
player_roster.append(player)
player = input('Who is your small forward?: ').title()
player_roster.append(player)
player = input('Who is your power forward?: ').title()
player_roster.append(player)

print('\n Your starting 5 for the upcoming basketball season:')
print(f'\t\t Point Guard: \t\t{player_roster[0]}')
print(f'\t\t Shooting Guard: \t{player_roster[1]}')
print(f'\t\t Center: \t\t{player_roster[2]}')
print(f'\t\t Small Forward: \t{player_roster[3]}')
print(f'\t\t Power Forward: \t{player_roster[4]}')

player_hurt = player_roster.pop(2)
print(f'\nOh no! {player_hurt} is hurt!')

print(f'\nYour roster now only has {len(player_roster)} players!')

player_new = input('\nWho will take his place?: ').title()
player_roster.insert(2, player_new)

print('\n\t Your NEW starting 5 for the upcoming basketball season:')
print(f'\t\tPoint Guard: \t\t{player_roster[0]}')
print(f'\t\tShooting Guard: \t{player_roster[1]}')
print(f'\t\tCenter: \t\t{player_roster[2]}')
print(f'\t\tSmall Forward: \t\t{player_roster[3]}')
print(f'\t\tPower Forward: \t\t{player_roster[4]}')

print(f'\nGood luck {player_roster[2]}, you will do great!')
print(f'Your roster is now at {len(player_roster)} players.  Good job!')