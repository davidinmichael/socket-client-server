import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "192.168.68.60"
PORT = 9999
s.connect((HOST, PORT))
while True:
    welcome = s.recv(1024)
    print("Server: ", welcome)
    data=input("Enter message to send: ")
    s.sendall(data.encode())