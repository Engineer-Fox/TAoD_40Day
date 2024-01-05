# Inheritance lesson
# Parent class and a child class

class Dog():
    '''A Class to represent a general dog'''
    def __init__(self,name,gender,age,loud):
        '''Initialize attributes'''
        self.name = name
        self.gender = gender
        self.age = age
        self.loud = loud #  Bool

    def call_dog(self):
        '''Call the dog'''
        if self.gender == 'male':
            print(f'Here {self.name}!  Good boy!')
        else:
            print(f'Here {self.name}!  Good girl!')
    
    def dog_years(self):
        '''Compute age in dog years'''
        dog_years = self.age*7
        print(f'{self.name} is {str(dog_years)} years old in dog years!')

    def bark(self):
        '''Get dog to speak'''
        if self.loud:
            print('WOOF WOOF WOOF!!!!')
        else:
            print('Woof.')

# A child class, Labrador

class Labrador(Dog):
    '''New class for Labrador breed of Dog'''
    def __init__(self, name, gender, age, loud, gunshy):
        super().__init__(name, gender, age, loud)
        self.gunshy = gunshy # Bool value

    def bark(self):
        '''Get dog to speak'''
        if self.loud:
            print('AHWOOOO AHWOOOO!!!!')
        else:
            print('Grrr.')

    def gohunting(self):
        if not self.gunshy:
            print(f'{self.name} is going to be a great hunting dog!')
        else:
            print(f'{self.name} will not be hunting anytime soon...')

class Newfidor(Labrador):
    '''New child class to Labrador'''
    def __init__(self, name, gender, age, loud, gunshy):
        super().__init__(name, gender, age, loud, gunshy)

    def bark(self):
        '''Get dog to speak'''
        if self.loud:
            print('WOOOOOOOOOOF')
        else:
            print(('PANTING PANTING PANTING').lower())


my_dog = Dog('Moonshine','female',1,False)
print(my_dog.name)
print(my_dog.age)
my_dog.dog_years()
my_dog.bark()

puppy = Labrador('Mahi','female',50,True,False)
print(puppy.name)
print(puppy.age)
puppy.dog_years()
puppy.bark()
puppy.gohunting()
bigdog = Newfidor('Buck','male',3,True,True)
bigdog.dog_years()
bigdog.bark()
bigdog.gohunting()
