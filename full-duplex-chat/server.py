
import socket
import threading

HOST = ""
PORT = 9999
client_sockets = []

def handle_client(client_socket):
    client_sockets.append(client_socket)
    message = "Welcome to i-Light Server"
    client_socket.sendall(message.encode())

def send_message(client_sockets):
    while True:
        message = input("Enter Message: ")
        for sock in client_sockets:
            sock.sendall(message.encode())

def receive_message(client_socket, client_sockets):
    while True:
        client_message = client_socket.recv(1024).decode()
        print("\nClient: ", client_message)

        for sock in client_sockets:
            sock.sendall(client_message.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
s.bind((HOST, PORT))

s.listen(5)
print ('Listening on port', PORT )

while True:
    conn, addr = s.accept()
    print(f"Connection to {addr} Established Successfully")
    handle_client(conn)
    send_thread = threading.Thread(target=send_message, args=(client_sockets,))
    recv_thread = threading.Thread(target=receive_message, args=(conn, client_sockets))
    send_thread.start()
    recv_thread.start()
