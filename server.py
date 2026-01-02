import socket
import threading

#server create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#IP and listening port in server
host = "0.0.0.0"    #this IP-address can connect any other IP-addresses
port = 12345

#binding the both IP-address and port
server_socket.bind((host, port))

#waits for the client
server_socket.listen()
print("Server started. Waiting for the client...")

clients = {}

def handle_client(client_socket):
    while True:
        
        try:
            #obtains the message 
            message = client_socket.recv(1024).decode()

            if not message :
                break

            username = clients[client_socket]

            full_message = f"{username} : {message}"

            for c in clients:
                if c != client_socket:
                    c.send(full_message.encode())

        except:
            break

    left_user = clients[client_socket]
    del clients[client_socket]
    client_socket.close()


while True :
    #accepts the client to connect 
    client_socket, client_address = server_socket.accept()

    username = client_socket.recv(1024).decode()
    clients[client_socket] = username
    print(f"{username} is connected. ")


    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()




