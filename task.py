class Task:
    def __init__(self, task_id, name, deadline, priority, status="Not Completed"):
        self.task_id = task_id
        self.name = name
        self.deadline = deadline
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Task ID: {self.task_id}, Name: {self.name}, Deadline: {self.deadline}, Status: {self.status}"

    def mark_complete(self):
        self.status = "Completed"

    def is_overdue(self):
        from datetime import datetime
        current_time = datetime.now()
        return current_time > self.deadline and self.status != "Completed"
