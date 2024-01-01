# Local and global variables part 2

def remove_names(names):
    '''Remove a name from a list'''
    removed_name = names.pop()
    print('Goodbye ',removed_name.title(),'.')
    return names

friends = ['Dalton','Lindsay','Leo','Roman','Wyatt']
print(friends)
new_friends = remove_names(friends.copy())
print(new_friends)