import random
print('Welcome to the Rock Paper Scissor App!')

moves = ['rock','paper','scissor']
rounds = (int(input('How many rounds do you want to play?:  ')))
p_wins = 0
c_wins = 0

for n in range(rounds):
    print(f'\nRound {str(n+1)}')
    print(f'Player: {str(p_wins)}\tComputer: {str(c_wins)}')
    c_action = random.choice(moves)
    p_action = (input('What choice do you want to try? (rock, paper, or scissors):  ').lower())
    if p_action in moves:
        print(f"\tComputer: {c_action}")
        print(f'\tPlayer: {p_action}')
        # computer rock
        if p_action == 'rock' and c_action == 'rock':
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        elif p_action == 'paper' and c_action == 'rock':
            winner = 'player'
            phrase = 'Paper covers rock!'
        elif p_action == 'scissor' and c_action == 'rock':
            winner = 'computer'
            phrase = 'Rock smashes scissor!'
        # computer paper
        if p_action == 'rock' and c_action == 'paper':
            winner = 'computer'
            phrase = 'Paper covers rock!'
        elif p_action == 'paper' and c_action == 'paper':
            winner = 'tie'
            phrase = 'It is a tie. How boring!'
        elif p_action == 'scissor' and c_action == 'paper':
            winner = 'player'
            phrase = 'Scissor cuts paper!'
        # computer scissor
        if p_action == 'rock' and c_action == 'scissor':
            winner = 'user'
            phrase = 'Rock smashes scissor!'
        elif p_action == 'paper' and c_action == 'scissor':
            winner = 'computer'
            phrase = 'Scissor cuts paper!'
        elif p_action == 'scissor' and c_action == 'scissor':
            winner = 'tie'
            phrase = 'It is a tie. How boring!'
        # add wins or losses
        if winner == 'user':
            p_wins += 1
            print(f'You win round {str(n + 1)}!')
        elif winner == 'computer':
            c_wins += 1
            print(f'Computer wins round {str(n+1)}!')
        elif winner == 'tie':
            print(f'No winner in round {str(n+1)} :(')
    else:
        print('That is not a valid move, computer gets a point!')
        c_wins += 1

print(f'The total for the {str(rounds)} rounds played are: \n')
print(f'\tUser Wins: {str(p_wins)}')
print(f'\tComputer Wins: {str(c_wins)}')
print(f'\nThank you for playing!  Please come again!')