import random


def game(player_move, computer_move):
    # Draw Section
    if (player_move == computer_move):
        print('Its a Draw')
    # Player Choose Rock
    elif (player_move == 1 and computer_move == 3):
        print('Rock is the winner, Scissors is the loser')
    elif (player_move == 1 and computer_move == 2):
        print('Paper is the winner, Rock is the loser')
    # Player Choose Paper
    elif (player_move == 2 and computer_move == 1):
        print('Paper is the Winner, Rock is the loser')
    elif (player_move == 2 and computer_move == 3):
        print('Scissors is the Winner, Paper is the loser')
    # Player Choose Scissors
    elif (player_move == 3 and computer_move == 2):
        print('Scissors is the Winner, Paper is the loser')
    elif (player_move == 3 and computer_move == 1):
        print('Rock is the Winner, Scissors is the loser')


computer_move = random.choice([1, 2, 3])
names = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
player_move = int(input(
    'Enter the move you want to play :\n 1 for Rock\n 2 for Paper\n 3 for Scissors\n :'))

if player_move == 1 or player_move == 2 or player_move == 3:
    print(
        f'Computer Choose {names[computer_move]}\nPlayer Choose {names[player_move]}')
    game(player_move, computer_move)


# Player Choose Something Else
else:
    print('Enter a valid option')
