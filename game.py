import sys

from modules.config import Config
from modules.configure_player import Player
from modules.grid_input import Input
from modules.server_connection import Connection


class tictactoe:

    def __init__(self):
        
        self.player_one_symbol = None
        self.player_two_symbol = None


    def game_repeat(self):
        play_again = input("Would you like to play again? Y/N: ")
        print("============================================================")
                
        if play_again.upper() == "Y":
            self.game()
        
        elif play_again.upper() == "N":
            print("Thank you for playing the game!")
            input("Press any key to close the program...")
            sys.exit(0)

        else:
            print("Please enter Y/N!")
            print("============================================================")
            self.game_repeat()


    def game(self):
        
        Connection.check_connection()
        players = Player()
        
        player_one = input("Player One, Enter your username: ")
        player_two = input("Player Two, Enter your username: ")
        print("============================================================")

        if player_one.strip(" ") == "" or player_two.strip(" ") == "":
            print("Please provide username!")
            print("============================================================")
            self.game()

        player_turn = players.allocate_player(player_one, player_two)
        
        if player_turn == True:
            self.player_one_symbol = "X"
            self.player_two_symbol = "O"

        if player_turn == False:
            self.player_one_symbol = "O"
            self.player_two_symbol = "X"
        
        Input.grid_input(player_one, player_two, self.player_one_symbol, self.player_two_symbol)

        self.game_repeat()

