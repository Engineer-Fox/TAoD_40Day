print('Sec32_Final.py')

names = []
print(names)
print(bool(names))

names = ['Mike','John']
print(bool(names))

numbers = list(range(1,11))
print(numbers)
while numbers:
    numbers.pop()
    print(numbers)
print('All elements removed...')

numbers = [4,1,1,2,3,4,5,6,7,4,1,1,8,9,9,9,1,2,3,4,5,6,7,8,9,10] 
while 4 in numbers:
    numbers.remove(4)
    print(numbers)
print('All 4s removed')

flag1 = True
flag2 = True
while flag1:
    print('while loop #1 is running...')
    while flag2:
        print('While loop #2 is running...')
        choice = input('Continue running while loop #2? y/n: ')
        if choice.lower() != 'y':
            flag2 = False
            print('Ending while loop #2...')
    choice = input('Continue running while loop #1? y/n: ')
    if choice != 'y':
        flag1 = False
        print('Ending while loop #1 now...')
print('Loop complete')