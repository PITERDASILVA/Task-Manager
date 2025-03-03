from models.database import initialize_db
from view_model.task_viewmodel import TaskViewModel
from views.console_view import ConsoleView

def delete_task(task_viewmodel):
    task = task_viewmodel.get_all_tasks()
    ConsoleView.display_task(task)

    try: 
        task_id = int(input("Enter task id:" )) 
        task_viewmodel.delete_task(task_id)
        print("Task deleted")
    except ValueError:
        print("Invalid task id")


def delete_category(task_viewmodel):
    categories = task_viewmodel.get_all_categories()
    ConsoleView.display_categories(categories)

    try:
        category_name = input("Enter category id: ")
        task_viewmodel.delete_category(category_name)
        print("Category deleted")
    except ValueError:
        print("Invalid category id")

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
                category_name = input("Enter category name: ")
                if category_name.lower() == category_name:
                    title = input("Enter title: ")
                    description = input("Enter description: ")
                    due_state = input("Enter due state: ")
                    task_view_model.add_task(title, description, category_name, due_state)
                    print("Task added")
                else: 
                    print("Please add a category")
                    name = input("Enter category name: ")
                    task_view_model.add_category(name)
            
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
                delete_task(task_view_model)
            
            elif option == 6:
                delete_category(task_view_model)
            
            elif option == 7:
                break
        
        except ValueError:  
            print("Invalid option")

if __name__ == "__main__":
    main()  