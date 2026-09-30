"""Group tasks by their subject or category."""


class CategoryManager:
    def organize_by_subject(self, tasks):
        groups = {}
        for task in tasks:
            if task.subject not in groups:
                groups[task.subject] = []
            groups[task.subject].append(task)
        return groups

    def organize_by_category(self, tasks):
        groups = {}
        for task in tasks:
            if task.category not in groups:
                groups[task.category] = []
            groups[task.category].append(task)
        return groups
