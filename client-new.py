import socket
import threading
# Create a socket object
def sendmsg():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server's IP address and port
    print("Server Ip")
    server_ip = str(input())  # Change this to the IP address of the server
    print("Server Port common(8080)")
    server_port = int(input())  # Change this to the port the server is listening on

    # Connect to the server
    s.connect((server_ip, server_port))
    print("Connection established!")

    # Send a message to the server
    message = str(input())
    s.send(message.encode('utf-8'))

    # Close the socket
    s.close()


def listening():


    # Function to handle a client connection
    def handle_client(client_socket):
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break  # Connection closed by the client

            # Print the received data
            print(f"Received data from {client_socket.getpeername()}: {data.decode('utf-8')}")

            # Send a response back to the client
            response = "Hello, client!"
            client_socket.send(response.encode('utf-8'))

        # Close the client socket
        client_socket.close()

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port to listen on
    host = "119.56.98.214"  # localhost
    port = 8090

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections (max 5 clients in the queue)
    server_socket.listen(5)

    print(f"Server is listening on {host}:{port}")

    while True:
        # Accept a connection from a client
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

