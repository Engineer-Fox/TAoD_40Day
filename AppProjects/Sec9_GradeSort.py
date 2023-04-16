print('Welcome to the grade sorter app!')

# user_grade1 = input('What is your first grade? (0-100): ')
# user_grade2 = input('What is your second grade? (0-100): ')
# user_grade3 = input('What is your third grade? (0-100): ')
# user_grade4 = input('What is your fourth grade? (0-100): ')

user_grades = []

grade = int(input('What is your first grade? (0-100): '))
user_grades.append(grade)
grade = int(input('What is your second grade? (0-100): '))
user_grades.append(grade)
grade = int(input('What is your third grade? (0-100): '))
user_grades.append(grade)
grade = int(input('What is your fourth grade? (0-100): '))
user_grades.append(grade)

print('\n Your grades are: ' + str(user_grades))

user_grades.sort(reverse=True)
print('\n Your grades from highest to lowest are: ' + str(user_grades))

print('\n The lowest two grades will now be dropped.')
removed_grade = user_grades.pop()
print('Removed grade: ' + str(removed_grade))
removed_grade = user_grades.pop()
print('Removed grade: ' + str(removed_grade))

print('Your remaining grades are: ' + str(user_grades))
print('Nice work!  Your highest grade is: ' + str(user_grades[0]) + ' .')