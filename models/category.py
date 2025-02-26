import sqlite3

class Category: 
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = sqlite3.connect('task_manager.db')
        cursor = conn.cursor()         
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (self.name,))
        conn.commit()       
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('task_manager.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        conn.close()
        return categories
    
    @staticmethod
    def delete(category_id):
        conn = sqlite3.connect('task_manager.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        conn.commit()   
        conn.close()    