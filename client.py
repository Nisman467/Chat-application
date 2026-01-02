import socket
import threading

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_IP = "127.0.0.1"
port = 12345

client_server.connect((server_IP, port))
print("Connected with server...")


def receive():
    while True:

        try:
            reply = client_server.recv(1024).decode()
            print(" : ", reply)
        except:
            break


thread = threading.Thread(target= receive)
thread.start()

while True:
    message = input(" : ")
    client_server.send(message.encode())