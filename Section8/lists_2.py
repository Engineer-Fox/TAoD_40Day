colors = ['black', 'red', 'yellow', 'brown', 'white']

print(colors)
print(colors[2])
print(colors[3])

#changing an element of a list
colors[2] = 'pink'
print(colors)

#adding an element with .append()
colors.append('blue')

print(colors)
#adding an element at a specific indexes
colors.insert(3, 'purple')
print(colors)

colors.insert(3, 'yellow')
colors.insert(-1, 'yellow')
print(colors)

new_colors = colors

new_colors.remove('yellow')
# can only remove one instantiation at a time
new_colors.remove('yellow')

print(new_colors)

removed_color = new_colors.pop()
print('Removing (And storing...) the color '+removed_color)

bad_color = new_colors.pop(1)
print('The bad color is ' + bad_color)

print(colors)
del colors[0]
print(colors)

user_colors = []
user_colors.append(input('Enter a color: '))
user_colors.append(input('Enter a color: '))
user_colors.append(input('Enter a color: '))
print(user_colors)
