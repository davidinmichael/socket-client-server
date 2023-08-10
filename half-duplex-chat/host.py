
import socket
import threading

def handle_client(client_socket):
    message = "Welcome to i-Light Server"
    client_socket.sendall(message.encode())

    while True:
        try:
            client_message = client_socket.recv(1024).decode()
            print("Client: ", client_message)

            server_response = input("Enter Message: ")
            client_socket.sendall(server_response.encode())
        except:
            break
    client_socket.close()

HOST = ""
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Waiting for connection...")

while True:
    conn, addr = s.accept()
    print(f"Connection from {addr} successful")
    thread = threading.Thread(target=handle_client, args=(conn,)) # create a
    thread.start()
