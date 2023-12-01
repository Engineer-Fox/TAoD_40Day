print('Sec32_Moderate.py')

current_num = 1
while current_num <= 10:
    if current_num % 2 ==0: 
        print(f'{str(current_num)} is even!')
    else:
        print(f'{str(current_num)} is odd!')
    current_num += 1

is_num = 1
playing = True
while playing:
    if is_num % 3 ==0:
        print(f'{str(is_num)} is divisible by 3!')
    else:
        print(f'{str(is_num)} is not divisible by 3!')
    choice = input('Press enter to continue or q to quit')
    if choice.lower() == 'q':
        playing = False
    is_num += 1
print(is_num)
print('QUITTING')

num = 10
while num>0:
    num -=1
    if num %4 ==0:
        continue
    print(f'Current variable value: {str(num)}')
print('All Done!')