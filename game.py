import random
import sys

class tictactoe:

    def __init__(self):
        self.grid_list = [[" ", "|", " ", "|", " "],
                          [" ", "|", " ", "|", " "], 
                          [" ", "|", " ", "|", " "]]
        self.grid_numbers = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.win_list = [["A1", "B2", "C3"], ["A1", "B1", "C1"], ["A1", "A2", "A3"],
                         ["A2", "B2", "C2"], ["B1", "B2", "B3"], ["C1", "B2", "A3"],
                         ["A3", "B3", "C3"], ["C1", "C2", "C3"]]
        self.player_one_turns = []
        self.player_two_turns = []
        self.playerOneTurnCounts = []
        self.playerTwoTurnCounts = []
        self.toss_list = ["H", "T"]
        self.player_one_name = None
        self.player_two_name = None
        self.player_one_toss = None
        self.player_two_toss = None
        self.grid_number = None
        self.turn_list = []


    def grid(self):
        i = 0
        print("     " + "A" + "   " + "|" + "   " + "B" + "   " + "|" + "   " + "C")
        print("--------------------------")

        for row in self.grid_list:
            i = i + 1
            print(str(i)  + "|" +"   " + row[0] + "   " + row[1] + "   " + row[2] + "   " + row[3] + "   " + row[4])
            print("--------------------------")
    

    def grid_check_update(self):
        
        for i in range(0, len(self.grid_list)):
            for j in range(0, len(self.grid_list[i])):
                if self.grid_number == "A1" and i == 0 and j == 0:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()
                
                elif self.grid_number == "B1" and i == 0 and j == 2:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()

                elif self.grid_number == "C1" and i == 0 and j == 4:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()

                elif self.grid_number == "A2" and i == 1 and j == 0:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()

                elif self.grid_number == "B2" and i == 1 and j == 2:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()

                elif self.grid_number == "C2" and i == 1 and j == 4:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()

                elif self.grid_number == "A3" and i == 2 and j == 0:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()

                elif self.grid_number == "B3" and i == 2 and j == 2:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()

                elif self.grid_number == "C3" and i == 2 and j == 4:
                    if self.grid_list[i][j] == " ":
                        self.grid_list[i][j] = self.turn_list[-1]
                        self.win_check()

                    else:
                        print("A symbol has already been placed in the grid! Please re-check and enter an empty grid number!")
                        print("============================================================")
                        self.turn_list.pop()
                        self.game()

                elif self.grid_number not in self.grid_numbers:
                    print("Please enter valid grid number as instructed!")
                    print("============================================================")
                    self.turn_list.pop()
                    self.game()


    def win_check(self):

        if self.turn_list[-1] == "X":
            self.playerOneTurnCounts.append(self.grid_number)

        if self.turn_list[-1] == "O":
            self.playerTwoTurnCounts.append(self.grid_number)

        for win_combination in self.win_list:
            if len(self.playerOneTurnCounts) >= 3:
                if set(win_combination).issubset(set(self.playerOneTurnCounts)):
                    print(self.player_one_name + " has won the game!")
                    print("============================================================")
                    self.game_repeat()

            if len(self.playerTwoTurnCounts) >= 3:
                if set(win_combination).issubset(set(self.playerTwoTurnCounts)):
                    print(self.player_two_name, " has won the game!")
                    print("============================================================")
                    self.game_repeat()

            if len(self.playerOneTurnCounts) > 5 or len(self.playerTwoTurnCounts) > 4:
                print("The game is a draw!")
                print("============================================================")
                self.game_repeat()
                

    def game_repeat(self):
        play_again = input("Would you like to play again? Y/N: ")
                
        if play_again.upper() == "Y":
            self.game()
        
        elif play_again.upper() == "N":
            print("Thank you for playing the game!")
            input("Press any key to close the program...")
            sys.exit(0)

        else:
            print("Please enter Y/N!")
            self.game_repeat()
                

    # def toss_decision(self):
    #     self.player_one_toss = input(self.player_one_name + ", Please enter H or T: ")
    #     if self.player_one_toss.upper() == "H":
    #         self.player_two_toss = "T"
    #         print(self.player_two_name + ", Tails(T) has been choosen for you by default.")
        
    #     elif self.player_one_toss.upper() == "T":
    #         self.player_two_toss = "H"
    #         print(self.player_two_name + ", Heads(H) has been choosen for you by default.")

    #     else:
    #         print(self.player_one_name + " please select H or T accordingly!")
    #         print("============================================================")
    #         self.toss_decision()


    def set_player(self):
        print("To start the game, the players must input their username!")
        print("============================================================")
        self.player_one_name = input("Please enter your display name (Player One): ")
        self.player_two_name = input("Please enter your display name (Player Two): ")
        print("============================================================")
        # print("To decide the first start, a toss will be done!")
        # print("============================================================")
        # self.toss_decision()
        # print("============================================================")
        print(self.player_one_name + ", You have been assigned symbol \"X\" by default.")
        print(self.player_two_name + ", You have been assigned symbol \"O\" by default.")
        print("============================================================\n")
        self.game()
        print("============================================================")

    
    def game(self):
        # choice = random.choice(self.toss_list)

        print("Choose the grid number where you want to place your symbol(grid number is letter followed by number i.e. (A1)): ")
        print("============================================================")
        
        while len(self.turn_list) < 9:
            self.grid()

            if len(self.turn_list) == 0:
                self.grid_number = input(self.player_one_name + ", Enter the grid number: ")
                print("============================================================")
                self.turn_list.append("X")

            else:
                if self.turn_list[-1] == "X":
                    self.grid_number = input(self.player_two_name + ", Enter the grid number: ")
                    print("============================================================")
                    self.turn_list.append("O")

                elif self.turn_list[-1] == "O":
                    self.grid_number = input(self.player_one_name + ", Enter the grid number: ")
                    print("============================================================")
                    self.turn_list.append("X")

            self.grid_check_update()
            print(self.playerOneTurnCounts)
            print(self.playerTwoTurnCounts)

