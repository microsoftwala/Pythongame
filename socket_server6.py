import threading
import socket


def calling(clinet_number):
    thread = threading.Thread(target=handle_client, args=(
        connections[client_number-1], addresses[client_number-1]))
    thread.start()


IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "BYE"

# List to store client connections and addresses
connections = []
addresses = []
sizes = 0
# Function to handle individual clients
option = []


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    while connected:
        try:
            msg = conn.recv(SIZE).decode(FORMAT)
            print(msg)
            option.append(msg)
            if msg == DISCONNECT_MSG:
                connections.remove(conn)
                addresses.remove(addr)
                print(connections, addresses)
                connected = False
            else:
                length = len(connections)

                for i in range(0, len(connections)):
                    if conn != connections[i]:
                        connections[i].send(msg.encode(FORMAT))
                # elif length == 3:
                #     for i in range(0, len(connections)):
                #         for j in range(0, len(connections)):
                #             if i != j:
                #                 connections[i].send(option[i].encode(FORMAT))

        except ConnectionResetError:
            print(f"[{addr}] Client connection forcibly closed.")
            connections.remove(conn)
            addresses.remove(addr)
            break

    conn.close()


print("[Starting] server is starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"[Listening] Server is listening on {IP}:{PORT}")

while True:
    conn, addr = server.accept()

    connections.append(conn)
    addresses.append(addr)

    # Assign the client number based on the number of connections
    client_number = len(connections)
    calling(client_number)  # Call the function to handle the client

    print(f"[Active connections] {threading.active_count() - 1}")
