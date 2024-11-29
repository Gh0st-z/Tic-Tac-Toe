import random
import socket

from modules.config import Config

class Multiplayer:

    def __init__(self, mode="offline"):

        self.conn = None
        self.client_socket = None
        self.client_address = None
        self.room_code = None
        self.player_name = None
        self.opponent_name = None
        self.mode = mode


    def generate_room_code(self):

        self.room_code = random.randint(100000, 999999)
        return self.room_code


    def create_room(self):

        if self.mode == "host":

            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((Config.SERVER_IP, Config.SERVER_PORT))
            server_socket.listen(1)
            room_code = self.generate_room_code()

            print(f"Room created. Share this code with your opponent: {room_code}")
            print("Waiting for a player to join...")
            print("============================================================")

            self.conn, self.client_address = server_socket.accept()
            received_code = self.conn.recv(1024).decode()
            if received_code != str(room_code):
                print("Incorrect room code entered by the player. Connection refused.")
                print("============================================================")
                self.conn.close()
                return False

            self.conn.send("OK".encode())

            self.player_name = input("Enter your username: ")
            print("============================================================")
            print("Please wait while the other player enters their username...")
            print("============================================================")
            self.conn.send(self.player_name.encode())
            self.opponent_name = self.conn.recv(1024).decode()
            print(f"You are playing against: {self.opponent_name}")
            print("============================================================")
            return True
        
        return False


    def join_room(self):

        if self.mode == "client":

            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((Config.SERVER_IP, Config.SERVER_PORT))
            room_code = input("Enter the 6-digit room code: ")
            self.client_socket.send(room_code.encode())

            response = self.client_socket.recv(1024).decode()
            if response == "OK":

                print("Connected to the game room!")
                print("============================================================")
                print("Please wait while the other player enters username...")
                print("============================================================")
                
                self.opponent_name = self.client_socket.recv(1024).decode()
                self.player_name = input("Enter your username: ")
                print("============================================================")
                self.client_socket.send(self.player_name.encode())
                print(f"You are playing against: {self.opponent_name}")
                self.conn = self.client_socket
                return True
                
            else:

                print("Incorrect room code. Connection refused.")
                print("============================================================")
                self.client_socket.close()
                return False
            
        return False


    def send_move(self, move):

        if self.conn:
            self.conn.send(move.encode())
        elif self.client_socket:
            self.client_socket.send(move.encode())


    def receive_move(self):

        if self.conn:
            return self.conn.recv(1024).decode()
        elif self.client_socket:
            return self.client_socket.recv(1024).decode()
