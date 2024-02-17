import os
def player_menu():
    print("===== Player Menu =====")
    print("1 Player Guess")
    print("2 Player Guess")
    print("3 Player Guess")
    print("4 Player Guess")
    print("Exit Game")
def execute_command(choice):
    if choice == '1':
        os.system("start game with 1 Player Guess")
    elif choice == '2':
        os.system("start game with 2 Player Guess")
    elif choice == '3':
        os.system("start game with 3 Player Guess")
    elif choice == '4':
        os.system("start game with 4 Player Guess")
    elif choice == '5':
        print("Exiting the game...")
    else:
        print("Invalid choice. Please select a valid option.")