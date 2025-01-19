class Calendar:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def view_calendar(self):
        # Display tasks in a calendar view
        tasks = self.task_manager.get_tasks_for_today()
        for task in tasks:
            print(task)
