import random
user_command = input("Choose [r]ock, [p]aper or [s]cissors: ").lower()

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
result = ''

if user_command == 'r':
    player_move = rock
elif user_command == 'p':
    player_move = paper
elif user_command == 's':
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

if player_move == rock:
    if computer_move == rock:
        result = 'd'
    elif computer_move == paper:
        result = 'l'
    elif computer_move == scissors:
        result = 'w'
elif player_move == paper:
    if computer_move == rock:
        result = 'w'
    elif computer_move == paper:
        result = 'd'
    elif computer_move == scissors:
        result = 'l'
elif player_move == scissors:
    if computer_move == rock:
        result = 'l'
    elif computer_move == paper:
        result = 'w'
    elif computer_move == scissors:
        result = 'd'

if result == 'w':
    print(f'The computer chose {computer_move}.')
    print('You win!')
elif result == 'd':
    print(f'The computer chose {computer_move}.')
    print('Draw!')
elif result == 'l':
    print(f'The computer chose {computer_move}.')
    print('Defeat!')
