import random
 
#define thesauraus
thesaurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
 
}
 
#messages
print("Welcome to the Thesaurus App!")
print("\nChoose a word from the thesaurus and I will give you a synonym.")
print("\nHere are the words in the thesaurus:")
 
#output keyd
for key in thesaurus.keys():
    print(f"\t-{key}")
 
# get selection and display random value
choice = input ("What word would you like a synonym for: ").strip().lower()
if choice in thesaurus.keys():
    words = thesaurus[choice]
    # This was the issue with my code, it seems like the range was incorrect
    index = random.randint(0, len(words)-1)
    print("A synonym for " + choice + " is " + words[index] + ".")
 
# print error if choice is not in the dictionary
else:
    print("not there")
 
# ask if they want to display the thesaurus
answer = input("\nWould you like to see the whole thesaurus (yes/no): ").lower().strip()
if answer.startswith("y"):
    for key, values in thesaurus.items():
        print("\n" + key +" synonyms are:")
        for value in values:
            print("\t-" + value)
 
else:
    print("I hope you enjoyed the program. Thank you!")