import random

class Player:

    def allocate_player(self, player_one, player_two):

        player_one_username = player_one
        player_two_username = player_two
        player_one_toss = None
        toss_list = ['H', 'T']

        print("Let's decide who starts first with a toss!")
        print("============================================================")

        player_one_toss = input(player_one_username + " , Enter your decision of heads or tails (H or T): ")
        print("============================================================")

        if random.choice(toss_list).upper() == player_one_toss:
            print(player_one_username + " has won the toss!")
            print("============================================================")
            return True
        
        elif player_one_toss not in toss_list:
            print("Enter H or T accordingly!")
            print("============================================================")
            self.allocate_player(player_one_username, player_two_username)

        else:
            print(player_two_username + " has won the toss!")
            print("============================================================")
            return False
        