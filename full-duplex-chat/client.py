import socket
import threading

def send_message(client_socket):
    while True:
        message = input("Enter Message: ")
        client_socket.sendall(message.encode())

def receive_message(client_socket):
    while True:
        client_message = client_socket.recv(1024).decode()
        print("Client: ", client_message)

HOST = "192.168.68.60"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

send_thread = threading.Thread(target=send_message, args=(s,))
recv_thread = threading.Thread(target=receive_message, args=(s,))
send_thread.start()
recv_thread.start()