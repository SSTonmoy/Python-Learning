'''The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.
'''
'''I will build a guessing game.'''


import random
def game():
    result = random.randint(1, 100)
    return result


with open('Chapter09/Hi-score.txt', 'r') as f:
    high_score = f.read()

old_high_score = 0 if high_score == '' else int(high_score)

current_score = game()
print(f'Your current score is {current_score}')

if current_score > old_high_score:
    with open('Chapter09/Hi-score.txt', 'w') as f:
        f.write(str(current_score))
else:
    print('Privious Score is Better')
