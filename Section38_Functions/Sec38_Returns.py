# What are return values

def calc_age(age, interval=0):
    age += interval
    # Anything after a return statement will not be run
    return age
    # print('hi') will not be run since it is after return
def course_info(course_name, student_count, credit_hours):
    '''Simulate a college course and return summary as a dict'''
    course = {
        'Course Name':course_name.title(),
        'Student Count':student_count,
        'Credit Hours':credit_hours,
        }
    return course
def drop_student(course):
    '''Simulate dropping a student from a specific course'''
    course['Student Count'] -= 1
    print(f"Dropping student from {course['Course Name']}.")


calc_age(33,10)

# Local vs global variables
# AGe and interval are not defined outside of the calc_age function, so cannot call them
new_age = calc_age(33,10)
print(new_age)

python = course_info('python programming',21,3)
for key, value in python.items():
    print(key,':',value)

drop_student(python)
for key, value in python.items():
    print(key,':',value)