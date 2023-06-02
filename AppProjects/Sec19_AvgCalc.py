print('Welcome to the GPA calculator app!')

user_name = input('What is your name?:  ')
grade_cnt = int(input('How many grades would you like to enter?:  '))
grade_list = []
for n in range(1, grade_cnt+1):
    grade_cnt.append(int(input('Enter grade: ')))
    print(str(n))

