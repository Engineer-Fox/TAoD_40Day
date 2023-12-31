# What is a function

# print('first argument','second argument','third argument')
# print('first argument','second argument','third argument', sep='$')

# First function created
def hello_world(name, age):
    """Greet the whole world"""
    print(f'Hello, {name.title()}!')
    print(f'You are, {str(age)} years old!')
def goodbye_world(name='User',day='Today'):
    """Say goodbye to a person and wish them a good day"""
    print(f'Goodbye {name.title()}...')
    print(f'May you have a great {day.title()} !')
def calc_age(age=0, interval=10):
    """Calculate the persons age in x years."""
    age = int(input('How old are you right now?: '))
    interval = int(input('How long from now would you like to know your age?: '))
    print(f'You are currently {str(age)} years old!')
    age += interval
    print(f'In {str(interval)} years, you will be {str(age)} years old!')

hello_world('Dalton',33)
goodbye_world()
goodbye_world('Dalton',)
goodbye_world('Dalton','Wednesday')
calc_age()