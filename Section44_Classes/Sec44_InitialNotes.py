#  Creating a class

class Baby():
    '''A simple class to simulate a baby'''
    #  Init method for the class Baby
    def __init__(self,name,sex,age):
        # Initialize attributes
        self.name = name.title()
        self.sex = sex
        self.age = age

        self.tired = True
    
    def play(self):
        pass

    def cry(self):
        pass

    def sleep(self):
        pass

little_boy = Baby('John','male',3)
little_girl = Baby('mary','female',5)
print(little_boy.name)