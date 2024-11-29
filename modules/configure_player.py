import random

class Player:

    def __init__(self, connection=None, client_address=None):

        self.conn = connection
        self.client_address = client_address


    def allocate_player(self, player_one, player_two, multiplayer=None):

        toss_list = ['H', 'T']

        if multiplayer and multiplayer.mode == "host":
            
            player_one_toss = input(f"{player_one}, choose heads or tails (H/T): ").strip().upper()

            while player_one_toss not in toss_list:
                player_one_toss = input("Invalid Input. Please choose H or T: ").strip().upper()

            toss_result = random.choice(toss_list)
            print(f"The toss result is: {toss_result}")

            if toss_result == player_one_toss:

                print(f"{player_one} wins the toss and will start first!")
                self.conn.send(f"Toss:{toss_result}:O".encode())
                return True
            
            else:

                print(f"{player_two} wins the toss and will start first!")
                self.conn.send(f"Toss:{toss_result}:X".encode())
                return False
            
        elif multiplayer and multiplayer.mode == "client":
            
            print(f"Please wait {player_one} is performing a toss!")
            print("============================================================")
            toss_info = self.conn.recv(1024).decode()
            toss_result, assigned_symbol = toss_info.split(":")[1:]

            print(f"The toss result is: {toss_result}")
            print(f"You have been assigned '{assigned_symbol}'")
        
        else:

            player_one_toss = input(f"{player_one}, choose heads or tails (H/T): ").strip().upper()
            while player_one_toss not in toss_list:
                player_one_toss = input("Invalid input. Please choose H or T: ").strip().upper()

            toss_result = random.choice(toss_list)
            print(f"The toss result is: {toss_result}")

            if toss_result == player_one_toss:
                print(f"{player_one} wins the toss and will start first!")
                print("============================================================")
                return True
            else:
                print(f"{player_two} wins the toss and will start first!")
                print("============================================================")
                return False