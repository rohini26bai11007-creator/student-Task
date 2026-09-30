"""Student Task and To-Do Manager command-line application."""

from task_manager import TaskManager
from status_manager import StatusManager
from category_manager import CategoryManager
from report_manager import ReportManager
from validators import clean_text, positive_integer
from utils import show_tasks, show_groups


def read_required(prompt, field_name):
    while True:
        try:
            return clean_text(input(prompt), field_name)
        except ValueError as error:
            print(error)


def add_task(manager):
    print("\nAdd a task")
    title = read_required("Task title: ", "Title")
    subject = read_required("Subject: ", "Subject")
    category = read_required("Category (for example, Assignment): ", "Category")
    due_date = read_required("Due date (enter a date or 'Not set'): ", "Due date")
    description = input("Description (optional): ").strip()
    task = manager.add_task(title, subject, category, due_date, description)
    print("Task added with number", task.task_id)


def read_task_number():
    while True:
        try:
            return positive_integer(input("Task number: "))
        except ValueError as error:
            print(error)


def print_menu():
    print("\n=== Student Task & To-Do Manager ===")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Search tasks")
    print("4. Mark task completed")
    print("5. View pending tasks")
    print("6. View completed tasks")
    print("7. Delete task")
    print("8. Organize by subject or category")
    print("9. Show statistics")
    print("0. Exit")


def run():
    manager = TaskManager()
    status_manager = StatusManager()
    category_manager = CategoryManager()
    report_manager = ReportManager()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task(manager)
        elif choice == "2":
            show_tasks(manager.get_all_tasks())
        elif choice == "3":
            word = read_required("Search title, subject, category or description: ", "Search")
            show_tasks(manager.search_tasks(word))
        elif choice == "4":
            task = manager.find_task(read_task_number())
            if status_manager.mark_completed(task):
                print("Task marked completed.")
            else:
                print("No task has that number.")
        elif choice == "5":
            show_tasks(status_manager.get_pending(manager.get_all_tasks()))
        elif choice == "6":
            show_tasks(status_manager.get_completed(manager.get_all_tasks()))
        elif choice == "7":
            if manager.delete_task(read_task_number()):
                print("Task deleted.")
            else:
                print("No task has that number.")
        elif choice == "8":
            kind = input("Organize by (1) subject or (2) category? ").strip()
            if kind == "1":
                show_groups(category_manager.organize_by_subject(manager.get_all_tasks()))
            elif kind == "2":
                show_groups(category_manager.organize_by_category(manager.get_all_tasks()))
            else:
                print("Choose 1 or 2.")
        elif choice == "9":
            report = report_manager.make_report(manager.get_all_tasks())
            print("Total:", report["total"])
            print("Completed:", report["completed"])
            print("Pending:", report["pending"])
        elif choice == "0":
            print("Goodbye, Rohini!")
            break
        else:
            print("Invalid choice. Choose a number from the menu.")


if __name__ == "__main__":
    run()
