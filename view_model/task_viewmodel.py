from models.task import Task
from models.category import Category

class TaskViewModel:
    def __init__(self):
        self.tasks = Task.get_all()
        self.categories = Task.get_all()

    def add_task(self, title, description, category_id, due_state):
        task = Task(title, description, category_id, due_state)
        task.save()
        self.tasks = Task.get_all()
    
    def delete_task(self, task_id):
        Task.delete(task_id)   
        self.tasks = Task.get_all()

    def add_category(self, name):
        category = Category(name)
        category.save()
        self.categories = Category.get_all()

    def delete_category(self, category_id):
        Category.delete(category_id)
        self.categories = Category.get_all()
    

    def get_all_tasks(self):
        return self.tasks
    
    def get_all_categories(self):  
        return self.categories