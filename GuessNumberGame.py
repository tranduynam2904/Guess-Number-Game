
import random
import time
def guess_number_game():
    while True:
        # Create a random choice number
        smallest_number = int(input("Enter the smallest number: "))
        highest_number = int(input("Enter the highest number: "))
        number_of_players = int(input("Enter the number of player: "))
        if smallest_number >= highest_number:
            print(f"Smallest number must not be greater than highest number")
        # elif number_of_players =
        else:
            break
    random_number = random.randint(smallest_number, highest_number)
    while True:
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
            print(f"You win! It is {random_number}")
            break
        if smallest_number == highest_number:
            print(f"You lose! It is {random_number}")
            break


guess_number_game()
