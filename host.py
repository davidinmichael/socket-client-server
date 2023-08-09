
import socket

HOST = ""
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
with conn:
    print(f"Connection from {addr} accepted")
    welcome = "Welcome to i-Light Server"
    conn.sendall(welcome.encode())
    while True:
        cmd = input("Enter message: ")
        if cmd == "quit" or cmd == "exit":
            conn.close()
            s.close()
        else:
            conn.sendall(cmd.encode())
            client_response = conn.recv(1024).decode()
            print("Client: ", client_response)
            # client_response = str(conn.recv(1024), "utf-8")
            # print(client_response, end="")
