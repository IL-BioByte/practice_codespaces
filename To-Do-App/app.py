import sqlite3

#initializing database and creating table 
def init_bd():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0,
        deadline TEXT,
        category TEXT
    )
''')

    conn.commit()
    conn.close()

init_bd()
