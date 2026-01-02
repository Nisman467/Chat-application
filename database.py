import sqlite3

def store_message(username, message):

    conn = sqlite3.connect("message_store.db", check_same_thread = False)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO storeMsg (sender, receiver) VALUES(?, ?)",(username,message))

    conn.commit()
    conn.close()

def view_message():
    
    conn = sqlite3.connect("message_store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM storeMsg")

    result = cursor.fetchall()

    for records in result:
        print(records) 

    conn.close()


# view_message()