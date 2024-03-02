import os


def player_menu():
    print("===== Player Menu =====")
    print("1. 1 Player Guess")
    print("2. 2 Player Guess")
    print("3. 3 Player Guess")
    print("4. 4 Player Guess")
    print("5. Exit Game")


def execute_command():
    choice = input("Please select an option: ")
    if choice == '1':
        os.system("echo Starting game with 1 Player Guess")
    elif choice == '2':
        os.system("echo Starting game with 2 Player Guess")
    elif choice == '3':
        os.system("echo Starting game with 3 Player Guess")
    elif choice == '4':
        os.system("echo Starting game with 4 Player Guess")
    elif choice == '5':
        print("Exiting the game...")
        exit()  # Exit the program
    else:
        print("Invalid choice. Please select a valid option.")
        return None

    return choice

