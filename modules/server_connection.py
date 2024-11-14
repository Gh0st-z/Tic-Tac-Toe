import socket

from modules.config import Config

class Connection:

    def check_connection():

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((Config.SERVER_IP, Config.SERVER_PORT))

        print("Checking for players on LAN please wait...")
        print("============================================================")

        response = client.recv(1024)
        response = response.decode("utf-8")

        if response.lower() == "accepted":
            print("Connection with server has been established!")
            print("============================================================")

        else:
            print("Could not establish connection with the server!")
            print("============================================================")

