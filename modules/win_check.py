class Win:

    def check_winner(grid_number, player_one_moves, player_two_moves, turn_list, player_one_symbol, player_two_symbol):

        win_list = [["A1", "B2", "C3"], ["A1", "B1", "C1"], ["A1", "A2", "A3"],
                         ["A2", "B2", "C2"], ["B1", "B2", "B3"], ["C1", "B2", "A3"],
                         ["A3", "B3", "C3"], ["C1", "C2", "C3"]]

        if turn_list[-1] == player_one_symbol:
            player_one_moves.append(grid_number)
        
        if turn_list[-1] == player_two_symbol:
            player_two_moves.append(grid_number)


        for win_combination in win_list:

            if len(player_one_moves) >= 3:  
                if set(win_combination).issubset(set(player_one_moves)):
                    return "Player One"

            if len(player_two_moves) >= 3:
                if set(win_combination).issubset(set(player_two_moves)):
                    return "Player Two"
                
            if len(player_one_moves) > 4:
                return("draw")
