import re
import socket
import threading

def receive_message(client_socket):
    while True:
        try:
            server_response = client_socket.recv(1024).decode()
            print("Server: ", server_response)

            data=input("Enter message to send: ")
            client_socket.sendall(data.encode())
        except:
            break
    client_socket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "192.168.68.60"
PORT = 9999
s.connect((HOST, PORT))
print('Connected')

receive_thread = threading.Thread(target=receive_message, args=(s,))
receive_thread.start()

# while True:
#     data=input("Enter message to send: ")
#     s.sendall(data.encode())