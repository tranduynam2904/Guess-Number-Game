import random
import time
import PlayerMenu


def guess_number_game():
    PlayerMenu.player_menu()
    number_of_players = PlayerMenu.execute_command()

    if number_of_players:
        print("\nPlayer 1, please set up the number range")
    # Create a limit number
    smallest_number = int(input("Enter the smallest number: "))
    highest_number = int(input("Enter the highest number: "))
    while smallest_number >= highest_number:
        print("Smallest number must not be greater than highest number")
        print("Please enter again!")
        smallest_number = int(input("Enter the smallest number: "))
        highest_number = int(input("Enter the highest number: "))
    random_number = random.randint(smallest_number, highest_number)
    while True:
        for player in range(1, int(number_of_players) + 1):
            print(f"Player {player}'s turn: ")
            user_number = int(input(f"Guess a number from {smallest_number} to {highest_number}: "))
            if user_number < smallest_number or user_number > highest_number:
                print(f"Number have to be between {smallest_number} and {highest_number}")
                time.sleep(0.5)
                print("Please enter again!")
            elif user_number < random_number:
                smallest_number = user_number + 1
                print(f"\nNew Range from {smallest_number} to {highest_number}")
            elif user_number > random_number:
                highest_number = user_number - 1
                print(f"\nNew Range from {smallest_number} to {highest_number}")
            else:
                print(f"\nPlayer {player} wins! It is {random_number}")
                return  # End the game when someone win

            if smallest_number >= highest_number:
                print(f"No one wins this round! The number was {random_number}")
                break  # Break the loop


guess_number_game()
