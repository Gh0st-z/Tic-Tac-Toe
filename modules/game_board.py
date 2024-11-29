from modules.win_check import Win

class Grid:

    def __init__(self):
        self.grid_list = [[" ", "|", " ", "|", " "],
                          [" ", "|", " ", "|", " "], 
                          [" ", "|", " ", "|", " "]]


    def create_board(self):

        grid_list = self.grid_list

        i = 0
        print("     " + "A" + "   " + "|" + "   " + "B" + "   " + "|" + "   " + "C")
        print("--------------------------")

        for row in grid_list:
            i = i + 1
            print(str(i)  + "|" +"   " + row[0] + "   " + row[1] + "   " + row[2] + "   " + row[3] + "   " + row[4])
            print("--------------------------")


    def grid_input(self, player_one, player_two, player_one_symbol, player_two_symbol, multiplayer=None):

        position_map = {
                            "A1": (0, 0), "B1": (0, 2), "C1": (0, 4),
                            "A2": (1, 0), "B2": (1, 2), "C2": (1, 4),
                            "A3": (2, 0), "B3": (2, 2), "C3": (2, 4)
                        }
        turn_list = []
        player_one_moves = []
        player_two_moves = []
        players = {player_one_symbol: player_one, player_two_symbol: player_two}
        symbols_order = [player_one_symbol, player_two_symbol] if player_one_symbol == "X" else [player_two_symbol, player_one_symbol]

        print("Choose the grid number where you want to place your symbol(grid number is letter followed by number i.e. (A1)): ")
        print("============================================================")

        while len(turn_list) < 9:
            
            self.create_board()

            current_symbol = symbols_order[len(turn_list) % 2]
            current_player = players[current_symbol]

            if multiplayer and multiplayer.mode in ["host", "client"]:

                is_host_turn = (multiplayer.mode == "host" and current_player == multiplayer.player_name)
                is_client_turn = (multiplayer.mode == "client" and current_player == multiplayer.player_name)
                
                if is_host_turn or is_client_turn:
                    
                    valid_move = False
                    while not valid_move:
                        grid_number = input(f"{current_player}, enter your move: ").strip().upper()
                        print("============================================================")
                        if grid_number in position_map and self.grid_list[position_map[grid_number][0]][position_map[grid_number][1]] == " ":
                            valid_move = True
                            multiplayer.send_move(grid_number)
                        else:
                            print("Invalid or already occupied grid. Try again.")
                            print("============================================================")
                else:
                    
                    print(f"Waiting for {current_player} to make a move...")
                    print("============================================================")
                    grid_number = multiplayer.receive_move()
                    print(f"{current_player} chose {grid_number}.")
                    print("============================================================")
                
            else:
                grid_number = input(f"{current_player}, enter your move: ").strip().upper()

            try:
                turn_list.append(current_symbol)
                self.check_update(grid_number, position_map, turn_list)

            except ValueError:
                continue

            winner = Win.check_winner(grid_number, player_one_moves, player_two_moves, turn_list, player_one_symbol, player_two_symbol)

            if winner:
                self.create_board()
                print(f"{current_player} wins!")
                print("============================================================")
                return
            
            if winner == "draw":
                print("It's a draw!")
                print("============================================================")



    def check_update(self, grid_number, position_map, turn_list):

        grid_number = grid_number.upper()

        if grid_number not in position_map:
            print("Please enter a valid grid number as instructed!")
            print("============================================================")

        row, col = position_map[grid_number]

        if self.grid_list[row][col] != " ":
            print("A symbol has already been placed in the grid! Please re-check and enter and empty grid number!")
            print("============================================================")
            turn_list.pop()

        self.grid_list[row][col] = turn_list[-1]
        return(self.grid_list)
    