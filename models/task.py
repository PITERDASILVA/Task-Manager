import sqlite3
import os 

class Task:
    def __init__(self, title, description, category_name ,due_state):
        self.title = title
        self.description = description
        self.category_name = category_name
        self.due_state = due_state
    
    def save(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'task_manager.db')
                               
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, category_name, due_state) VALUES (?, ?, ?, ?)",
                          (self.title, self.description, self.category_name, self.due_state)) 
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        base_dir = os.path.dirname(os.path.abspath(__file__))   
        db_path = os.path.join(base_dir, 'task_manager.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return tasks
    
    @staticmethod
    def delete(task_id):
        base_dir = os.path.dirname(os.path.abspath(__file__))   
        db_path = os.path.join(base_dir, 'task_manager.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()