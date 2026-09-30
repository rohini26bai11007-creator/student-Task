"""Task class used by the Student Task and To-Do Manager."""


class Task:
    """Store the details and status of one student task."""

    def __init__(self, task_id, title, subject, category, due_date, description=""):
        self.task_id = task_id
        self.title = title
        self.subject = subject
        self.category = category
        self.due_date = due_date
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def get_status(self):
        if self.completed:
            return "Completed"
        return "Pending"

    def __str__(self):
        return (f"[{self.task_id}] {self.title} | Subject: {self.subject} | "
                f"Category: {self.category} | Due: {self.due_date} | {self.get_status()}")
