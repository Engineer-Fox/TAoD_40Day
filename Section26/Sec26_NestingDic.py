# Nesting Dictionaries

user_0 = {
    'name':'john',
    'age':22,
}

user_1 = {
    'name':'bill',
    'age':21
}

user_2 = {
    'name':'ted',
    'age':21
}
users = [user_0,user_1,user_2]
for user in users:
    for key, value in user.items():
        print(f'Name: {key} \t\tAge: {str(value)}')
    print('\n')
users = []
for user in range(100):
    new_user = {'name':'NA','age':0}
    users.append(new_user)

for user in users[:10]:
    print(user)

friends = {
    'bill':['john','tom','harry'],
    'tom':['john','harry','bill'],
    'mary':['sue','bill','tom'],
}
for key, values in friends.items():
    print(f"\n{key.title()}'s friends are: ")
    for values in friends.items():
        print(f"\t\t{values}")

user_directory = {
    'm.smith':{
        'first_name':'matt',
        'last_name':'smith',
        'age':31
        },
    'd.fox':{
        'first_name':'dalton',
        'last_name':'fox',
        'age':33,
        }
    }

for user, info in user_directory.items():
    print(f'\nUsername: {user}')
    for key, value in info.items():
        print(f'{key}: {str(value)}')