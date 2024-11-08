import game
import sys

game_obj = game.tictactoe()

def menu():
    try:
        print("============================================================")
        print("Hello and Welcome to TicTacToe!")
        print("============================================================")
        game_mode = int(input("What would you like to play today!\n" +
                        "1. Player Vs Player \n" +
                        "2. Player Vs CPU \n" +
                        "3. Quit \n" +
                        "Please select a game mode: "))
        print("============================================================")

        if game_mode == 1:
            game_obj.set_player()

        elif game_mode == 2:
            print("This game mode is yet to be released!")
            print("============================================================")
            menu()

        elif game_mode == 3:
            print("Thank you for playing the game!")
            input("Press any key to close the program...")
            sys.exit(0)

        else:
            print("Please enter valid input from 1 to 3!")
            menu()
    
    except ValueError:
        print("Please enter valid input from 1 to 3!")
        menu()

menu()