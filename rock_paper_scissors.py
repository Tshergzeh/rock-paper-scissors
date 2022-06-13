import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return f"It's a tie! Computer also chose {expand(computer)}."

    if is_win(user, computer):
        return f'You won! Computer chose {expand(computer)}.'
    
    return f'You lost! Computer chose {expand(computer)}.'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def expand(letter):
    if letter == 'r':
        return 'rock'
    elif letter == 'p':
        return 'paper'
    return 'scissors'

print(play())