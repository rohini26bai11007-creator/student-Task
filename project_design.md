# Project Design

## Program flow

`main.py` creates the managers and repeatedly displays a numbered menu. A menu choice calls the relevant manager or display helper. The program ends when the user chooses Exit.

## Modules and responsibilities

| Module | Responsibility |
| --- | --- |
| `main.py` | Menu, input prompts and coordination |
| `task.py` | Task fields and completion status |
| `task_manager.py` | Add, find, search, list and delete tasks |
| `status_manager.py` | Mark completed and filter pending/completed tasks |
| `category_manager.py` | Group tasks by subject or category |
| `report_manager.py` | Calculate task totals |
| `validators.py` | Check required text and positive task numbers |
| `utils.py` | Display tasks and groups |

## Data design

Each `Task` object stores an integer task number, title, subject, category, due-date text, optional description and a Boolean completion value. `TaskManager` keeps task objects in a list and assigns increasing task numbers. Grouping methods return dictionaries whose keys are subject or category names and whose values are lists of tasks.

## Input checks

Required text is stripped of surrounding spaces and cannot be blank. Task numbers are converted to integers and must be positive. If the requested task number does not exist, the program reports this and continues. Menu choices are checked before an operation is selected.

## Syllabus boundary

The design uses introductory Python fundamentals, operators, input/output, conversion and `type()`, lists, tuples, sets, dictionaries, frozensets, control flow, functions, modules/packages, array data structure and OOP as permitted course concepts. The implementation only needs lists and dictionaries for task storage and grouping. It uses Python's standard library for the requested tests and does not require third-party packages, a database, GUI, web app, API, AI or advanced framework.

## Possible future improvement

Saving tasks to a plain text file could be considered only if it is allowed by the course requirements.
