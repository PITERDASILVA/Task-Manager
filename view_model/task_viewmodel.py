from models.task import Task
from models.category import Category

class TaskViewModel:
    def __init__(self):
        self.tasks = Task.get_all()
        self.categories = Task.gel_all()

    def add_task(self, title, description, category_id, due_state):
        task = Task(title, description, category_id, due_state):
        task.save()
        self.tasks = Task.get_all()

    def gel_all_task(self):
        return self.tasks
    
    def get_all_categories(self):  
        return self.categories