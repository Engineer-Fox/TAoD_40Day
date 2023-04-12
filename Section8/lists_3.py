#sorting lists and the len() function
sports = ['footbal', 'hockey', 'baseball', 'soccer', 'Tennis']
print(sports)
#sorted in a print statement is temporary 
# print(sorted(sports))
# print(sorted(sports, reverse=True))
sports.sort(reverse=True)
print(sports)

grades = [88, 99, 77, 66]
print(grades)
print(len(grades))

grades.sort()
print(grades)