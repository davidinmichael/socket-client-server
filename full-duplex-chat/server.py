from concurrent.futures import thread
import socket
import threading

HOST = ""
PORT = 9999

def send_message(client_socket):
    while True:
        message = input("Enter Message: ")
        client_socket.sendall(message.encode())

def receive_message(client_socket):
    while True:
        client_message = client_socket.recv(1024).decode()
        print("\nClient: ", client_message)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
s.bind((HOST, PORT))

s.listen(5)
print ('Listening on port', PORT )

while True:
    conn, addr = s.accept()
    print(f"Connection to {addr} Established Successfully")
    send_thread = threading.Thread(target=send_message, args=(conn,))
    recv_thread = threading.Thread(target=receive_message, args=(conn,))
    send_thread.start()
    recv_thread.start()
