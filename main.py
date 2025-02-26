from models.database import initialize_db
from view_model.task_viewmodel import TaskViewModel
from views.console_view import ConsoleView
from models.category import Category

def menu():
    print("\nTask Manager")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Add category") 
    print("4. Display categories")
    print("5. Delete task")
    print("6. Delete category")
    print("7. Exit")

def main():
    initialize_db()
    task_view_model = TaskViewModel()


    print("Categories")
    categories = task_view_model.get_all_categories()
    ConsoleView.display_categories(categories)

    print("\nTasks:")
    tasks = task_view_model.get_all_tasks()
    ConsoleView.display_task(tasks)

    while True:
        try:
            menu()
            option = int(input("Enter option: "))
            if option == 1:
                title = input("Enter title: ")
                description = input("Enter description: ")
                category_id = int(input("Enter category id: "))
                due_state = input("Enter due state: ")
                task_view_model.add_task(title, description, category_id, due_state)
                print("Task added")
            
            elif option == 2:
                tasks = task_view_model.get_all_tasks()
                ConsoleView.display_task(tasks)
            
            elif option == 3:
                name = input("Enter category name: ")
                task_view_model.add_category(name)

            elif option == 4:
                categories = task_view_model.get_all_categories()
                ConsoleView.display_categories(categories)

            elif option == 5:
                task_id = int(input("Enter task id: ")) 
                task_view_model.delete_task(task_id)
                print("Task deleted")
            
            elif option == 6:
                category_id = input("Enter category id: ")
                if category_id in Category.get_all():
                    task_view_model.delete_category(category_id)
                    print("Category deleted")
                else:
                    print("Category not found")
            
            elif option == 7:
                break
        
        except ValueError:  
            print("Invalid option")

if __name__ == "__main__":
    main()  