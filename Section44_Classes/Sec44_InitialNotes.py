#  Creating a class
import random
class Baby():
    '''A simple class to simulate a baby'''
    #  Init method for the class Baby
    def __init__(self,name,sex,age):
        # Initialize attributes
        self.name = name.title()
        self.sex = sex.lower()
        self.age = age

        self.tired = True
    
    def play(self):
        if self.sex == 'male':
            print(self.name + ' is playing with cars.')
        else:
            print(self.name + ' is playing with blocks.')

    def cry(self):
        '''Simulate crying'''
        print('WAAAH WAAAH WAAAH')
        print('even ' + str(self.age)+ ' year olds cry.')
        
    def sleep(self):
        if self.tired:
            print(self.name + ' is sleeping... FINALLY!')
            self.tired = False

        else:
            print('Sorry! ' + self.name + ' is not tired...')

little_boy = Baby('John','male',3)
little_girl = Baby('mary','female',5)
print(little_boy.name+' is a '+str(little_boy.age)+' year old '+little_boy.sex+'.')
print(little_girl.name+' is a '+str(little_girl.age)+' year old '+little_girl.sex+'.')
little_boy.play()
little_girl.play()
little_boy.sleep()
little_girl.sleep()
little_boy.sleep()

babies = []
for i in range(1,101,1):
    num = random.randint(0,1)
    if num == 0:
        sex = 'male'
    else:
        sex = 'female'
    age = random.randint(0,5)
    baby = Baby(str(i),sex, age)
    babies.append(baby)

for baby in babies:
    print(baby.name + ' is a '+str(baby.age)+' year old '+ baby.sex+'.')