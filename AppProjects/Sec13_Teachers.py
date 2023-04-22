print('Welcome to the Favorite Teacher(s) Program/App!')

favorite = []

new_favorite = input('Who is your first favorite teacher?: ').title()
favorite.insert(0, new_favorite)
new_favorite = input('Who is your second favorite teacher?: ').title()
favorite.insert(1, new_favorite)
new_favorite = input('Who is your third favorite teacher?: ').title()
favorite.insert(2, new_favorite)
new_favorite = input('Who is your fourth favorite teacher?: ').title()
favorite.insert(3, new_favorite)

print(f'\nYour favorite teachers are {favorite} !')
favorite.sort()
print(f'Your favorite teachers alphabetically are {favorite} !')
favorite.sort(reverse=True)
print(f'Your favorite teachers reverse alphabetically are {favorite} !')
print(f'Your top two favorite teachers are {favorite[0]} and {favorite[1]}!')
print(f'Your next two favorite teachers are {favorite[2]} and {favorite[3]}!')
print(f'Your least favorite teacher is {favorite[3]}!')
print(f'\nYou have {len(favorite)} favorite teachers total!')

dropped_teacher = favorite.pop(3).title()
replacement = input(f'Oops!  {dropped_teacher} is no longer your least favorite teach...  Who will be your least favorite now?: ').title()
favorite.insert(3, replacement)
print(f'\n Great choice! {replacement} will make an excellent favorite teacher!')
print(f'\nYour new list of favorite teachers is: {favorite}!')