from models.database import initialize_db
from view_model.task_viewmodel import TaskViewModel
from views.console_view import ConsoleView


def main():
    initialize_db()
    task_view_model = TaskViewModel()

    print("Categories")
    categories = task_view_model.get_all_categories
    ConsoleView.display_categories(categories)

    print("\nTasks:")
    tasks = task_view_model
    ConsoleView.display_task(tasks)

if __name__ == "__main__":
    main()  