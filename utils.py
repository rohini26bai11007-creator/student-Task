"""Small display helpers for task lists and grouped tasks."""


def show_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    for task in tasks:
        print(task)
        if task.description:
            print("    Description: " + task.description)


def show_groups(groups):
    if not groups:
        print("No tasks to organize.")
        return
    for name in groups:
        print("\n" + name + ":")
        show_tasks(groups[name])
