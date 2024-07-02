import sqlite3

def createTable():
    # Create a database connection
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create a table in the database
    c.execute('''CREATE TABLE IF NOT EXISTS data (name TEXT, date TEXT, time TEXT, data TEXT)''')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

def storeData(name, date, time, data):
    # Create a database connection
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Insert data into the database
    c.execute("INSERT INTO data (name, date, time, data) VALUES (?, ?, ?, ?)", (name, date, time, data))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()