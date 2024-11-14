from modules.game_board import Board
from modules.grid_update import Grid
from modules.win_check import Win

class Input:

    def grid_input(player_one, player_two, player_one_symbol, player_two_symbol):

        grid_list = [[" ", "|", " ", "|", " "],
                          [" ", "|", " ", "|", " "], 
                          [" ", "|", " ", "|", " "]]
        grid_numbers = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        position_map = {
                            "A1": (0, 0), "B1": (0, 2), "C1": (0, 4),
                            "A2": (1, 0), "B2": (1, 2), "C2": (1, 4),
                            "A3": (2, 0), "B3": (2, 2), "C3": (2, 4)
                        }
        turn_list = []
        grid_number = None
        playerOneTurnCounts = []
        playerTwoTurnCounts = []

        print("Choose the grid number where you want to place your symbol(grid number is letter followed by number i.e. (A1)): ")
        print("============================================================")

        while len(turn_list) < 9:
            try:
                Board.create_board(grid_list)

                if len(turn_list) == 0:
                    if player_one_symbol == "X":
                        grid_number = input(player_one + ", Enter the grid number: ")
                        print("============================================================")
                        turn_list.append(player_one_symbol)

                    if player_two_symbol == "X":
                        grid_number = input(player_two + ", Enter the grid number: ")
                        print("============================================================")
                        turn_list.append(player_two_symbol)

                else:
                    if turn_list[-1] == player_one_symbol:
                        grid_number = input(player_two + ", Enter the grid number: ")
                        print("============================================================")
                        turn_list.append(player_two_symbol)

                    elif turn_list[-1] == player_two_symbol:
                        grid_number = input(player_one + ", Enter the grid number: ")
                        print("============================================================")
                        turn_list.append(player_one_symbol)

                grid_list = Grid.check_update(grid_list, grid_number, grid_numbers, position_map, turn_list)
                win = Win.win_check(turn_list, player_one_symbol, player_two_symbol, grid_number, player_one, player_two, playerOneTurnCounts, playerTwoTurnCounts)
                
                if win == player_one:
                    print(player_one + " has won the game!")
                    print("============================================================")
                    break

                elif win == player_two:
                    print(player_two + " has won the game!")
                    print("============================================================")
                    break

                elif win == "draw":
                    print("The game is a draw!")
                    print("============================================================")
                    break

            except KeyError:
                turn_list.pop()
                pass