"""Functions for changing and filtering task status."""


class StatusManager:
    def mark_completed(self, task):
        if task is None:
            return False
        task.mark_completed()
        return True

    def get_pending(self, tasks):
        return [task for task in tasks if not task.completed]

    def get_completed(self, tasks):
        return [task for task in tasks if task.completed]
