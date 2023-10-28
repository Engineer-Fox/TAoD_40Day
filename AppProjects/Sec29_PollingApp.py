print('Welcome to the Polling App!')

topic = input(f'What is the yes or no issue you will be voting on today?: ')
topic_vote_qty = int(input('How many voter will you allow to vote on the topic?: '))
topic_pw = input('Enter the password for the polling results: ')

yes = 0
no = 0
results = {}
for i in range(topic_vote_qty):
    votername = input('\nEnter your full name: ')
    if votername in results.keys():
        print('Sorry, it seems that someone with that name has already cast a vote on this topic.')
    else:
        print(f'Here is our topic: {topic}')
        vote_choice = input('What do you think?  Yes or No?: ').lower().strip()
        if vote_choice == 'yes' or vote_choice == 'y':
            vote_choice = 'yes'
            yes +=1
        elif vote_choice == 'no' or vote_choice == 'n':
            vote_choice = 'no'
            no +=1
        else:
            print(f'That is not a yes or no choice, but okay...')
        # Add vote to the dictionary results
        results[votername] = vote_choice
        print(f'Thank you {votername} your vote of {vote_choice} has been recorded!')
# Show who voted
total_votes = len(results.keys())
print(f'n\The following {total_votes} people voted: ')
for key in results.keys():
    print(key)
# Summarize the results
print(f'\nOn the following issue: {topic}')
if yes > no:
    print(f'Yes wins! {str(yes)} votes to {str(no)}.')
elif no > yes:
    print(f'No wins! {str(no)} votes to {str(yes)}.')
elif yes == no:
    print(f'It was a tie... {str(yes)} votes to {str(no)}.')

# Allow admin to see actual votes
guess = input(f'\nTo see the voting results, enter the admin password: ')
if guess == topic_pw:
    for key, value in results.items():
        print(f'Voter: {key} \t\tVote: {value}')
else:
    print('Sorry that is not the correct password.  Goodbye.')

print('Thank you for using the voter polling app!')