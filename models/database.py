import sqlite3
import os

def initialize_db():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'task_manager.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS categories
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE
                   )
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT, 
                   description TEXT, 
                    category_name TEXT, 
                    due_state TEXT,
                    FOREIGN KEY(category_name) REFERENCES categories(name))''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
