# Three key statements for looping, break, continue, pass

# for n in range(1,11):
#     if n == 5:
#         print(f'Your number is {str(n)}!')
#     else:
#         print(n)
for n in range(1,11):
    if n == 8:
        break
    elif n == 5:
        continue
    elif n == 6:
        pass
    else:
        print(n)

#break stops the whole loop
# continue stops the current iteration of the loop
# pass will pass over the current statement and continues the loop as normal
