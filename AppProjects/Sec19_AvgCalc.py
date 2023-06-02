print('Welcome to the GPA calculator app!')
#prompt user to input name, qty of grades to calc avg
# THIS DOES NOT ADD WEIGHT TO VALUES
user_name = input('What is your name?:  ')
grade_cnt = int(input('How many grades would you like to enter?:  '))
grade_list = []
for n in range(1, grade_cnt+1):
    grade_list.append(int(input('Enter grade: ')))
#Forgot the reverse syntax, and the method needs the boolean in the parenth!
grade_list.sort(reverse=True)
print('Your grades from highest to lowest are: ')
for grade in grade_list:
    print(f'\t {str(grade)}')
#making our own average function instead of importing an external library like numpy
grade_avg = sum(grade_list)/len(grade_list)

print(f"\n {user_name}'s Grade Summary:")
print(f'\t Total Numer of Grades (Entered by {user_name}): {str(grade_cnt)}')
print(f'\t Highest Grade: {max(grade_list)}')
print(f'\t Lowest Grade: {min(grade_list)}')
print(f'Average: {str(grade_avg)}')

desired_grade = float(input(f'\n What is your desired average?: '))
needed_grade = (desired_grade*(len(grade_list)+1))-(sum(grade_list))
print(f'Good luck {user_name}!')
print(f'You will need a {str(needed_grade)} on your final, to reach your desired grade in the class!')

print('Lets see what your average could have been if you did better or worse on your assignments.')

#need to create a new list so we can append/remove without changing the original
new_grades = grade_list[:]
grade_pick = int(input('What grade would you like to change?: '))
grade_change = int(input(f'What grade would you like to change {str(grade_pick)} to?: '))
new_grades.remove(grade_pick)
new_grades.append(grade_change)
#creating new print statements for the new variables
#new average and difference between new and old avg to be printed below
new_avg = sum(new_grades)/len(new_grades)
avg_diff = grade_avg - new_avg
print(f"\n {user_name}'s NEW Grade Summary:")
print(f'\t New Total Numer of Grades (Entered by {user_name}): {str(len(new_grades))}')
print(f'\t New Highest Grade: {max(new_grades)}')
print(f'\t New Lowest Grade: {min(new_grades)}')
print(f'\t New Average: {str(new_avg)}')
print(f'Your new average would be {str(new_avg)} compared to your real average of {str(grade_avg)}!  \n Which is a change of {avg_diff}!')
#final print to the user about extra credit
print('\n Too bad your original grades are still the same!')
print(grade_list)
print(f'\n You should ask for at least {avg_diff} points of extra credit!')