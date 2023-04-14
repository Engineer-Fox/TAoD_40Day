#An introduction to lists

#square brackets
topics = ['Physics','Comp Sci', 'Algebra', 'Art', 'History', 'Relationship and Spirituality', 'Modern Lit', 'Contemporary Lit']

print(topics)
print(type(topics))


topics_2 = ['Art', 'History', 'Relationship and Spirituality', 'Modern Lit', 'Contemporary Lit']
print(topics_2)

#print function with the indexes in square brackets to call that element of the list
print(topics[2])
print(topics_2[2])

print(topics[-1]) #last element is denoted by -1, second to last is -2, etc.

print('My favorite class ever is ' + topics[-1].upper() + '!')