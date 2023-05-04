#using zip() function

names = ["jack", "john", "mark", "paul"]
numbers = [20,44,3,15]
for name in names:
    print(name)

for i in range(len(names)):
    print(names[i]+': '+str(numbers[i]))

for name, number in zip(names, numbers):
    print(name.title()+':'+str(number))
