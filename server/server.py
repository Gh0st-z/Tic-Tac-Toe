import socket
import sys

class Server:

    def __init__(self, host="127.0.0.1", port=8000):
        self.server_ip = host
        self.port = port


    def run_server(self):
        server_ip = self.server_ip
        port = self.port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            server.bind((server_ip, port))
        except socket.error as e:
            print("Failed to bind port: Another instance of the server may already be running.")
            server.close()
            sys.exit()

        server.listen(5)
        print(f"Server listening on {server_ip}:{port}")

        try:
            while True:
                client_socket, addr = server.accept()
                print(f"Accepted connection from {addr}")
                response = "accepted".encode("utf-8")
                client_socket.send(response)

        except KeyboardInterrupt:
            print("Shutting down server.")
        finally:
            server.close()
            

if __name__ == '__main__':
    server = Server()
    server.run_server()