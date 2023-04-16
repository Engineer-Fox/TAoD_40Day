print('\t\t Summary Table')

num_strings = ['15', '100', '55', '42']
print(f'\n The variable num_strings is a {type(num_strings)}.'
    f'\n It contains the elements: {str(num_strings)}'
    f'\n The element {num_strings[0]} is a {str(type(num_strings[0]))}.'
)
num_ints = [15, 100, 55, 42]
print(f'\n The variable num_ints is a {type(num_ints)}.'
    f'\n It contains the elements: {num_ints}'
    f'\n The element {num_ints[0]} is a {type(num_ints[0])}.'
)
num_floats = [2.2, 5.0, 1.245, 0.142857]
print(f'\n The variable num_floats is a {type(num_floats)}.'
    f'\n It contains the elements: {num_floats}'
    f'\n The element {num_floats[0]} is a {type(num_floats[0])}.'
)
num_lists = [[1,2,3], [4,5,6],[7,8,9]]
print(f'\n The variable num_lists is a {type(num_lists)}.'
    f'\n It contains the elements: {num_lists}'
    f'\n The element {num_lists[0]} is a {type(num_lists[0])}.'
)
num_strings.sort()
num_ints.sort()
    
print('\n Now sorting num_strings and num_ints...')
print(f'\t Sorted num_strings: {num_strings}')
print(f'\t Sorted num_ints: {num_ints}')

print('\n Strings are sorted alphabetically while integers are sorted numerically!')
