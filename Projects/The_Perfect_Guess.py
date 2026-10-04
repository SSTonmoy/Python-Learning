'''
We are going to write a program that generates a random number and asks the user to
guess it.
If the players guess is higher than the actual number, the program displays “Lower
number please” .
Similarly, if the users guess is too low, the program prints “Higher number please” .
When the user guesses the correct number, the program displays the number of
guesses the player used to arrive at the number
'''
import random
guess_number = random.randint(1, 100)
trial = 1
while True:
    player_number = int(input('Enter the number : '))
    if (guess_number == player_number):
        print(f'Congrats, you got it it trial number {trial}')
        break
    elif (guess_number < player_number):
        print('Lower Number Please')
        trial += 1
    elif (guess_number > player_number):
        print(' Higher Number Please')
        trial += 1
