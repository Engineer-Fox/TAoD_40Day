print('Sec32_Basics.py')

for i in range(1,10):
    print(i)

is_num = 1
while is_num <= 10:
    if is_num % 2 != 0:
        print(is_num)
    is_num += 1

current_num = 1
while True:
    print(current_num)
    current_num += 1
    choice = input('Press enter to print the next number or q to quit: ').lower()
    if choice == 'q':
        break