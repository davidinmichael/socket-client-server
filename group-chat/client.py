import socket
import threading

HOST = "192.168.68.60"
PORT = 9999
username = input("Choose a Username: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = s.recv(1024).decode()
            if message == "Username":
                s.sendall(username.encode())
            else:
                print(message)
        except:
            print("An error occurred")
            s.close()
            break

def send():
    while True:
        # message = f"{username}: {input("")}"
        message = input(f"{username}: ")
        s.sendall(message.encode())

recv_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

recv_thread.start()
send_thread.start()
