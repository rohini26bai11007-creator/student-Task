"""Operations for creating, finding, listing and deleting tasks."""


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, subject, category, due_date, description=""):
        from task import Task
        task = Task(self.next_id, title, subject, category, due_date, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        return self.tasks

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def search_tasks(self, word):
        results = []
        word = word.lower()
        for task in self.tasks:
            if (word in task.title.lower() or word in task.subject.lower()
                    or word in task.category.lower() or word in task.description.lower()):
                results.append(task)
        return results

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task is not None:
            self.tasks.remove(task)
            return True
        return False
