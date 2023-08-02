# Looping through a dictionary

fav_colors = {
    'John':'blue',
    'Gabe':'orange',
    'Mary':'yellow',
    'Mike':'Purple',
    'Lucas':'yellow',
    'Sarah':'green'
}

print(fav_colors)
fav_colors_list = fav_colors.items()
print(fav_colors_list)

for k, v in fav_colors.items():
    print(f'The key {k} has an associated value of {v}.')

fav_colors_keys = fav_colors.keys()
print(fav_colors_keys)

for name in fav_colors.keys():
    print(name.title() + ', Thank you for taking the survey!')
if 'brooke' not in fav_colors.keys():
    print('Brooke, you should take the Survey!')

for value in fav_colors.values():
    print(value)