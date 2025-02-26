import sqlite3

class Task:
    def __init__(self, title, description, category_id ,due_state):
        self.title = title
        self.description = description
        self.category_id = category_id
        self.due_state = due_state
    
    def save(self):
        conn = sqlite3.connect('task_manager.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, category_id, due_state) VALUES (?, ?, ?, ?)",
                          (self.title, self.description, self.category_id, self.due_state)) 
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('task_manager.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return tasks
    
    @staticmethod
    def delete(task_id):
        conn = sqlite3.connect('task_manager.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()