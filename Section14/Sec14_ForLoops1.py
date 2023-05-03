#This will be for the first video in section 14 on for loops.
# teams = ["giants", "bills", "jets", "patriots"]
# print(teams)
# print(type(teams))
# print(teams[0].title())
# print(teams[1].title())
# print(teams[2].title())
# print(teams[3].title())
# print("Go team! \n")

# for team in teams:
#     print(team.title())
# print('The loop is done, and your team is going to win! \n')
# could also be
#  for i in teams:
    #print(i.title()), where the i is the variable being called in each iteration of the loop

#for loop to iterate through integers function
values = [1,2,3,4,5]
total_sum = 0 # setting the initial value outside of the loop allows it to add after each iteration of the loop

for value in values:
    total_sum += value
print(total_sum)

#list of lists for loop
triples = [['a','b','c'], ['1','2','3'],['do','re','me']]

for list_value in triples:
    for element in list_value:
        print(element, end=' ')
    print('The loop is finished.  ALL DONE!')
print('We are officially done with the complete loop!')

