import os
import subprocess
import socket
import sys

from game import tictactoe
from modules.config import Config

game_obj = tictactoe()

def is_server_running(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            return True
        except socket.error:
            return False

def start_server():
    file_path = 'run_server.bat'
    
    if not is_server_running(Config.SERVER_IP, Config.SERVER_PORT):
        if os.path.exists(file_path):
            subprocess.run(f'start cmd /c {file_path}', shell=True)
        
        else:
            print("Server File is not present! Cannot start server!")

    else:
        print("Server is already running!")


def menu():

    start_server()
    
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
            game_obj.game()
            
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

    except ConnectionRefusedError:
        print("Please wait for the server to open!")
        menu()

menu()