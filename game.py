from modules.configure_player import Player
from modules.game_board import Grid
from modules.multiplayer import Multiplayer


class tictactoe:

    def __init__(self):
        
        self.player_one_symbol = None
        self.player_two_symbol = None


    def game_repeat(self):

        play_again = input("Would you like to play again? Y/N: ").strip().upper()
        print("============================================================")
                
        if play_again == "Y":
            self.game()
        
        elif play_again == "N":
            print("Thank you for playing the game!")
            input("Press any key to close the program...")
            exit()

        else:
            print("Please enter Y/N!")
            print("============================================================")
            self.game_repeat()


    def game(self):
        
        multiplayer = Multiplayer()
        players = Player()
        grid = Grid()

        print("Choose your game mode:\n",
              "1. Host a multiplayer game \n",
              "2. Join a multiplayer game \n",
              "3. Offline mode")
        user_input = int(input("Enter your choice (1/2/3): ").strip()) 
        print("============================================================")
        
        if user_input == 1:

            multiplayer.mode = "host"
            if multiplayer.create_room():
                self.start_game(multiplayer, grid, players)

        elif user_input == 2:

            multiplayer.mode = "client"
            if multiplayer.join_room():
                self.start_game(multiplayer, grid, players)
        
        elif user_input == 3:

            multiplayer.mode = "offline"
            player_one = input("Player One, Enter your username: ").strip()
            player_two = input("Player Two, Enter your username: ").strip()
            print("============================================================")

            if not player_one or not player_two:
                print("Player names cannot be empty. Try again.")
                self.game()

            self.start_offline_game(player_one, player_two, grid, players)
        
        else:
            print("Invalid choice. Please select a valid option.")
            self.game()


    def start_game(self, multiplayer, grid, players):

        players.conn = multiplayer.conn

        host_name = multiplayer.player_name if multiplayer.mode == "host" else multiplayer.opponent_name
        client_name = multiplayer.opponent_name if multiplayer.mode == "host" else multiplayer.player_name

        print("============================================================")
        print(f"Room Host: {host_name}")
        print(f"Room Client: {client_name}")
        print("Deciding who will start first with a coin toss...")
        print("============================================================")

        toss_winner = players.allocate_player(host_name, client_name, multiplayer)

        if toss_winner:
            self.first_player = host_name
            self.second_player = client_name

        else:
            self.first_player = client_name
            self.second_player = host_name

        self.player_one_symbol = "X"
        self.player_two_symbol = "O"

        if multiplayer.mode == "host":
            print("============================================================")
            print(f"{self.first_player} will start first as Player One with 'X'.")
            print(f"{self.second_player} will be Player Two with 'O'.")

        else:
            print("============================================================")
            print(f"{self.first_player} will start first as Player One with 'X'.")
            print(f"{self.second_player} will be Player Two with 'O'.")

        print("============================================================")

        grid.grid_input(
            self.first_player, self.second_player, self.player_one_symbol, self.player_two_symbol, multiplayer
        )
        self.game_repeat()


    def start_offline_game(self, player_one, player_two, grid, players):

        print(f"Player One: {player_one}")
        print(f"Player Two: {player_two}")
        print("Deciding who will start first with a coin toss...")
        print("============================================================")

        toss_winner = players.allocate_player(player_one, player_two)

        if toss_winner:
            self.first_player = player_one
            self.second_player = player_two

        else:  
            self.first_player = player_two
            self.second_player = player_one

        self.player_one_symbol = "X"
        self.player_two_symbol = "O"

        print(f"{self.first_player} will start first as Player One with 'X'.")
        print(f"{self.second_player} will be Player Two with 'O'.")
        print("============================================================")

        grid.grid_input(
            self.first_player, self.second_player, self.player_one_symbol, self.player_two_symbol
        )
        self.game_repeat()
