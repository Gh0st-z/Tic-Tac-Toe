class Win:

    def win_check(turn_list, player_one_symbol, player_two_symbol, grid_number, player_one, player_two, playerOneTurnCounts, playerTwoTurnCounts):

        win_list = [["A1", "B2", "C3"], ["A1", "B1", "C1"], ["A1", "A2", "A3"],
                         ["A2", "B2", "C2"], ["B1", "B2", "B3"], ["C1", "B2", "A3"],
                         ["A3", "B3", "C3"], ["C1", "C2", "C3"]]


        if turn_list[-1] == player_one_symbol:
            playerOneTurnCounts.append(grid_number)

        if turn_list[-1] == player_two_symbol:
            playerTwoTurnCounts.append(grid_number)

        for win_combination in win_list:
            if len(playerOneTurnCounts) >= 3:
                if set(win_combination).issubset(set(playerOneTurnCounts)):
                    return(player_one)

            if len(playerTwoTurnCounts) >= 3:
                if set(win_combination).issubset(set(playerTwoTurnCounts)):
                    return(player_two)

            if len(playerOneTurnCounts) > 4:
                return("draw")
