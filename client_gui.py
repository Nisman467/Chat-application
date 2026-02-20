import socket
import threading 
import customtkinter as ctk
from tkinter import simpledialog
from database import store_message


#Scoket create
Server_IP = "127.0.0.1"
port = 12345

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_server.connect((Server_IP, port))

##Appearence 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#gui setup
window_win = ctk.CTk()
window_win.title("Chat Application")
window_win.geometry("500x600")


username = simpledialog.askstring("Username", "Enter your name : ", parent=window_win)
if not username:
    username = "User"
client_server.send(username.encode())

header = ctk.CTkLabel(window_win, text= f"Logged in as : {username}", font=("Arial",15,"bold"))
header.pack(padx=10, pady=8)

chat_area = ctk.CTkScrollableFrame(window_win, width =360, height=300)
chat_area.pack(padx=10, pady=10, fill="both", expand=True)

message = ctk.CTkEntry(window_win, font=("Arial", 11), placeholder_text = "Type your message...")
message.pack(padx=10, pady=5, fill="x")
window_win.after(200, message.focus_set)

#Emoji panel (This is hidden by default so need the 😊 button)
emoji_frame = ctk.CTkFrame(window_win)

emojis = ["😀","😂","😎","❤️","👍","🎉","🤔","🥳","😭","😡"]

def insert_emoji(emoji):
    current_message = message.get()
    message.delete(0, "end")
    message.insert(0, f"{current_message}{emoji}")

for e in emojis:
    button = ctk.CTkButton(emoji_frame, text = e, width = 40, command = lambda em=e : insert_emoji(em))
    button.pack(side = "left", padx = 3, pady = 4)

#emoji button 
def toggle_emoji_panel():
    if emoji_frame.winfo_ismapped():
        emoji_frame.pack_forget()
    else:
        emoji_frame.pack(padx = 10, pady = 5, fill = "x")

emoji_button = ctk.CTkButton(window_win, text = "😄", command = toggle_emoji_panel, width = 40)
emoji_button.pack(pady = 4, side = "right")



#For bubble message
def add_message(message, sender):

    bubble = ctk.CTkFrame(chat_area, corner_radius = 12, 
                        fg_color = "#1f2937" if sender == "You" else "#2563eb")
    
    label = ctk.CTkLabel(bubble, text = message, wraplength = 220, justify = "left", text_color = "white")
    label.pack(padx = 10, pady = 6)

    ##anchor means align of the bubble message 
    if sender == "You":
        bubble.pack(anchor = "e", padx = 10, pady = 4)  #anchor = "e" --> left side if "you" send the message
    else:
        bubble.pack(anchor = "w", padx = 10, pady = 4)  #anchor = "w" -->right side if "other" send the message

    chat_area.update_idletasks()
    chat_area._parent_canvas.yview_moveto(1.0)

#Sending function to server
def send_message():
    message.focus_set()
    message_entry = message.get()
    if message_entry.strip() == "":
        return
    try:
        client_server.send(message_entry.encode())
        store_message(username, message_entry)
        message.delete(0, ctk.END)
        message.focus_set()
        add_message(message_entry, "You")
    except:
        pass

send_button = ctk.CTkButton(window_win, text="Send", command=send_message, font=("Arial", 10, "bold"))
send_button.pack(side="right", pady=0)

message.bind("<Return>", lambda event : send_message())

#receiving the message from the server
def receive_message():
    while True:
        try:
            reply = client_server.recv(1024).decode()
            add_message(reply, "others")
        except:
            break

thread = threading.Thread(target=receive_message, daemon=True)
thread.start()

window_win.mainloop()