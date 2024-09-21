import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

counter_win = 0
counter_draw = 0
counter_lose = 0
counter_first_input = 0

while True:
    user_command = input("\nChoose [r]ock, [p]aper, or [s]cissors: ").lower().strip()

    if user_command == 'r':
        player_move = rock
    elif user_command == 'p':
        player_move = paper
    elif user_command == 's':
        player_move = scissors
    else:
        print("Invalid Input. Please try again...")
        continue

    counter_first_input += 1

    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    if player_move == computer_move:
        result = 'd'
    elif (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        result = 'w'
    else:
        result = 'l'

    print(f"\nYou chose {player_move}. The computer chose {computer_move}.")

    if result == 'w':
        print("You win this round!")
        counter_win += 1
    elif result == 'd':
        print("It's a draw!")
        counter_draw += 1
    else:
        print("You lose this round!")
        counter_lose += 1

    print(f"Current score after game {counter_first_input}/3:\
    [Wins: {counter_win}] [Draws: {counter_draw}] [Losses: {counter_lose}]")

    if counter_first_input == 3:
        break

print("\n--- Final Result ---")
if counter_win > counter_lose:
    success_rate = (counter_win / 3) * 100
    print(f"Congratulations! You won the series with a success rate of {success_rate:.2f}%.")
elif counter_win == counter_lose:
    print("The series ends in a draw!")
else:
    success_rate = (counter_win / 3) * 100
    print(f"Sorry, you lost the series. Your success rate was {success_rate:.2f}%. Try again!")
