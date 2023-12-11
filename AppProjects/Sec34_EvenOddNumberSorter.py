print('Sec34_EvenOddNumberSorter.py')
running = True
#run the number sorter as long as the user wants
while running:
    num_string = input('Enter in a string of numbers separated by a comma (,): ')
    num_string = num_string.replace(' ','')
    num_list = num_string.split(',')
    print('\n----------Result Summary-----------')
    for i in num_list:
        i = int(i)
        if i % 2 != 0:
            print(f'{str(i)} is odd!')
        else:
            print(f'{str(i)} is even!')

    # make new list for the even or odd numbers
    even = []
    odd = []
    for i in num_list:
        i = int(i)
        if i % 2 !=0:
            odd.append(i)
        else:
            even.append(i)
    print(f'The following {str(len(even))} numbers are even:')
    for i in even:
        print(f'\t{i}')
    print(even)
    print(f'The following {str(len(odd))} numbers are odd:')
    for i in odd:
        print(f'\t{i}')
    print(odd)
    continue_going = input('Would you like to continue? (y/n):  ').lower().strip()
    if continue_going != 'y':
        # could be either break or running = False to end the while loop
        break
print('All done!')