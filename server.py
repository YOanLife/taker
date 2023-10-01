import socket

# Server configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345     # Port for the server to listen on

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            client_socket, client_addr = server_socket.accept()
            print(f"Connection from {client_addr}")

            with client_socket:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_server()

