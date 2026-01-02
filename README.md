# Chat Application (LAN Based)

A Python-based GUI chat application that allows multiple users to communicate
in real time over the same local network (LAN) using socket programming.

## Features
- Multi-client server
- GUI using Tkinter
- Username-based chat
- Send messages using Enter key
- Auto-scroll chat window
- SQLite database for message storage
- Works on same Wi-Fi / LAN

## Technologies Used
- Python
- Socket Programming
- Multithreading
- Tkinter
- SQLite3

## Project Files
- server.py       → Server program
- client_gui.py  → Client GUI application
- database.py    → Database handling
- requirements.txt
- README.md

## How to Run
inside the cmd prompt/ vs code terminal

### Start Server
python server.py

###Start Gui
python client_gui.py

### Use server IP as your LAN IP-address
SERVER_IP = "192.168.x.x"

## Create .exe file 

### Install the pyinstaller
```bash
pyinstaller --onefile --windowed client_gui.py
```
The executable file will be generated inside the dist/ folder.

## Notes

a) Allow Python through Windows Firewall (Private Network)
b) Server must be running before clients connect
c) .exe and database files are not included in this repository
