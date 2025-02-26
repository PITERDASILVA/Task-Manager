import sqlite3

def initialize_db():
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT, description TEXT, 
                    category_id INTEGER, 
                    due_state TEXT,
                    FOREIGN KEY(category_id) REFERENCES categories(id))''')
    
    conn.commit()
    conn.close()
