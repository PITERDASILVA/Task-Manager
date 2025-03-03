import sqlite3
import os


class Category: 
    def __init__(self, name):
        self.name = name

    def save(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'task_manager.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()         
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (self.name,))
        conn.commit()       
        conn.close()

    @staticmethod
    def get_all():
        base_dir = os.path.dirname(os.path.abspath(__file__))   
        db_path = os.path.join(base_dir, 'task_manager.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        conn.close()
        return categories
    
    @staticmethod
    def delete_by_name(category_name):
        base_dir = os.path.dirname(os.path.abspath(__file__))   
        db_path = os.path.join(base_dir, 'task_manager.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categories WHERE id = ?", (category_name,))
        conn.commit()   
        conn.close()    