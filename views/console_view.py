class ConsoleView:
    @staticmethod
    def display_task(tasks):
        if not tasks :
            print("Not tasks found")
            return
        for task in tasks:
            print(f'Tasks: {task[1]}\nDescription: {task[2]}\nCategory:{task[3]}\nDue State: {task[4]}\n')
    
    @staticmethod
    def display_categories(categories):
        if not categories:
            print("No categories found")
            return
        for category in categories:
            print(f"Category: {category[1]}")