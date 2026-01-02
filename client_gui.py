import socket
import threading 
import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog
from database import store_message

#Scoket create
Server_IP = "192.168.1.201"
port = 12345

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_server.connect((Server_IP, port))

#gui setup
window_win = tk.Tk()
window_win.title("Chat Application")
window_win.geometry("400x500")
window_win.resizable(False,False)

username = simpledialog.askstring("Username", "Enter your name : ", parent=window_win)
if not username:
    username = "User"
client_server.send(username.encode())

header = tk.Label(window_win, text= f"Logged in as : {username}")
header.pack(padx=10, pady=8)

chat_area = scrolledtext.ScrolledText(window_win)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state="disabled")

message = tk.Entry(window_win)
message.pack(padx=10, pady=5, fill=tk.X)
message.focus()


#Sending function to server
def send_message():
    message_entry = message.get()
    if message_entry.strip() == "":
        return
    try:
        client_server.send(message_entry.encode())
        store_message(username, message_entry)
        message.focus()
        message.delete(0, tk.END)
        chat_area.yview(tk.END)
        chat_area.config(state="normal")
        chat_area.insert(tk.END,f"You  :  {message_entry} \n")
        chat_area.config(state="disabled")
    except:
        pass

send_button = tk.Button(window_win, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

message.bind("<Return>", lambda event : send_message())

#receiving the message from the server
def receive_message():
    while True:
        try:
            reply = client_server.recv(1024).decode()
            chat_area.config(state="normal")
            chat_area.insert(tk.END, reply + "\n")
            chat_area.config(state="disabled")
        except:
            break

thread = threading.Thread(target=receive_message, daemon=True)
thread.start()

window_win.mainloop()