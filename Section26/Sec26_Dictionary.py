#Dictionaries continiued

bob_info = {
    "first_name":"Dalton",
    "last_name":"Fox",
    "age":32,
    "fav_colors":['green','orange','purple','red']
}

print(bob_info)
print(type(bob_info))

print(bob_info['age'])

bob_info['weight'] = 221
bob_info['height'] = 76.5

print(bob_info)
bob_info['weight'] -=6
print(f"Wow {bob_info['first_name']}, you lost some weight! You now weight {bob_info['weight']} pounds!")
bob_info['age'] += 1
print(f'Happy birthday {bob_info["first_name"]}! You are now {bob_info["age"]}!')

user_info = {}
user_info['name'] = input('What is your name:  ').title()
user_info['age'] = input('What is your age: ').title()
user_info['job'] = input('What is your job:  ').title()
print(user_info)