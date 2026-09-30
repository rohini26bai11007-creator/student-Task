# Student Task & To-Do Manager

A beginner-friendly command-line project by **Rohini Ghodeshwar**. Use it to keep track of school tasks, their subjects, categories, due dates and completion status.

## Requirements

Python 3 is required. The project uses only Python's built-in features; no package installation is needed.

## Run the program

Open a terminal in this folder and run:

```text
python main.py
```

Choose a menu number to add, view, search, complete, filter, delete, organize or count tasks. Choose `0` to exit. Tasks stay in memory while the program is running and are cleared when it exits.

## Run the tests

```text
python -m unittest discover -s tests -v
```

## Project files

- `main.py` displays the menu and connects the program parts.
- `task.py` defines one task.
- `task_manager.py` stores and finds tasks in a list.
- `status_manager.py` updates and filters task status.
- `category_manager.py` groups tasks by subject or category.
- `report_manager.py` counts tasks.
- `validators.py` checks text and number input.
- `utils.py` displays tasks and groups.
- `tests/test_project.py` checks the main operations.
- `statement.md` and `project_design.md` document the project.

## Concepts used

Variables, strings, input/output, type conversion, lists, dictionaries, loops, conditions, functions, modules, classes and objects, and basic error handling. The project has no GUI, web service, database, external package or API.
