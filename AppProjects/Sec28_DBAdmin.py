print(f'Welcome to the Database Admin App!')
# Enter your username
# Enter your password
# Hello username! You are logged in!
# Would you like to change your password:
# What would you like your new pw to be:
# new pw check; ham not the minimum eight characters
# username your password is new pw

UserInfo = {
    "dfox":'N@tives90',
    "dmoney":'N@tives90',
    "lfox":'N@tvies90',
    "admin00":'admin1234'
}

username = input(f'Enter your username: ').lower().strip()

if username in UserInfo.keys():
    password = input(f'Enter your password: ')
    if password == UserInfo[username]:
        print(f'Hello {username}! You are logged in!')
        if username == 'admin00':
            for key, value in UserInfo.items():
                print(f'\t- {key} \t {value}')
            print(f'We are oh so happy to see you, Lord Highness Admin! Please make yourself at home!')
        else:
            # allow non-admin user to login
            password_change = input(f'Would you like to change your password? (Yes/No):  ')
            if password_change.startswith('y'):
                new_pw = input(f'What would you like your new password to be? (Min 10 characters):  ')
                if len(new_pw) >= 10:
                    UserInfo[username] = new_pw
                else:
                    print(f'Your new password does not meet the requirements and only has {str(len(new_pw))} characters!')
                print(f'{username}, thanks for updating! Your password is now {new_pw}')
            else:
                print('Thank you!  Goodbye!')
    else:
        print(f'Password incorrect')
else:
    print(f'Username not in database.  Goodbye!')