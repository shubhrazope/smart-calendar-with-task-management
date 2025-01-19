from task import Task
from smart_calendar import Calendar
from reminder import Reminder
from gui import launch_gui
from database import Database

db = Database()
task_manager = Task(db)
calendar = Calendar(task_manager)
reminder_system = Reminder(task_manager)

# Launch the GUI for user interaction
launch_gui(task_manager, calendar, reminder_system)
