import random
player_choice = input('Enter rock, paper or scissor: ')
computer_choice = random.choice(['scissor', 'paper', 'rock'])
dict = {1: 'rock', 2: 'paper', 3: 'scissor'}

if player_choice == computer_choice:
    print('TIE')
elif player_choice == 'scissor' and computer_choice == 'paper':
    print('You WIN. Computer choice was', computer_choice, 'Scissor cuts paper')
elif player_choice == 'scissor' and computer_choice == 'rock':
    print('You LOSE. Computer choice was', computer_choice, 'Rock breaks scissor')
elif player_choice == 'rock' and computer_choice == 'paper':
    print('You LOSE. Computer choice was', computer_choice, 'Paper wraps rock')
else:
    print('Your choice was not valid')
