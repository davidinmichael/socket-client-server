import socket
import threading

HOST = ""
PORT = 9999
clients = []
usernames = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
print("Server started")
server_socket.listen(5)
print(f"Server is listening on {HOST}, Port {PORT}")

def broadcast(message):
    for client in clients:
        client.sendall(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode()
            broadcast(message.encode())
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames(index)
            broadcast(f"{username} left the group chat".encode())
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected to {address}")

        client.sendall("Username".encode())
        username = client.recv(1024).decode()

        clients.append(client)
        usernames.append(username)

        print(f"{username} just connected")
        broadcast(f"{username} joined the chat".encode())
        client.sendall("You can now send and receive messages in the group chat".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
