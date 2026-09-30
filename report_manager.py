"""Simple task counts and completion statistics."""


class ReportManager:
    def make_report(self, tasks):
        total = len(tasks)
        completed = 0
        for task in tasks:
            if task.completed:
                completed += 1
        return {"total": total, "completed": completed, "pending": total - completed}
