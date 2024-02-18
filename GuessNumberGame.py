import random
import time
import PlayerMenu


def guess_number_game():
    PlayerMenu.player_menu()
    number_of_players = PlayerMenu.execute_command()
    while True:
        # Create a random choice number
        smallest_number = int(input("Enter the smallest number: "))
        highest_number = int(input("Enter the highest number: "))
        if smallest_number >= highest_number:
            print(f"Smallest number must not be greater than highest number")
        # elif number_of_players =
        else:
            break
    random_number = random.randint(smallest_number, highest_number)
    for player in range(int(number_of_players)):
        while True:
            print(f"Player {player + 1}'s turn: ")
            # Create a user choice number
            # print(random_number)
            user_number = int(input(f"Guess a number from {smallest_number} to {highest_number}: "))
            if user_number < smallest_number or user_number > highest_number:
                print(f"Number have to between {smallest_number} and {highest_number}")
                time.sleep(0.5)
                print(f"Please enter again!")
            # Check the number
            elif user_number < random_number:
                smallest_number = user_number + 1
                print(f"New Range from {smallest_number} to {highest_number}")
            elif user_number > random_number:
                highest_number = user_number - 1
                print(f"New Range from {smallest_number} to {highest_number}")
            else:
                print(f"Player {player + 1} wins! It is {random_number}")

            # Check if smallest = highest
            if smallest_number == highest_number:
                print(f"No one win! It is {random_number}")
                break

guess_number_game()
