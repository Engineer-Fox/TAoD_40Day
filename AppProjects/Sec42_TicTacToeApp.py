'''Tic Tac Toe App'''

def draw_board(charlist):
    '''Print a game board'''
    print('\n\t\tTicTacToe')
    print('\t~~~~~~~~~~~~~~~~~~~~~~~')
    print('\t|| ', charlist[0],' || ',charlist[1],' || ',charlist[2],' ||')
    print('\t-----------------------')
    print('\t|| ', charlist[3],' || ',charlist[4],' || ',charlist[5],' ||')
    print('\t-----------------------')
    print('\t|| ', charlist[6],' || ',charlist[7],' || ',charlist[8],' ||')

def get_player_in(player_char, char_list):
    '''Get player info'''

def place_char_board():
    '''Place character on board'''
def is_winner():
    '''Determine winner of game'''
player1 = 'X'
player2 = 'O'
nlist = ['1','2','3','4','5','6','7','8','9']
clist = ['-']*9

draw_board(clist)
draw_board(nlist)