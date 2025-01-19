import smtplib
from email.mime.text import MIMEText

class Reminder:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def send_reminder(self, task):
        # Send email reminder for an upcoming task
        if task.is_overdue():
            message = MIMEText(f"Reminder: Task {task.name} is overdue!")
            message['Subject'] = f"Reminder: {task.name}"
            message['From'] = 'youremail@example.com'
            message['To'] = 'recipient@example.com'

            with smtplib.SMTP('smtp.example.com') as server:
                server.login('youremail@example.com', 'password')
                server.sendmail('youremail@example.com', 'recipient@example.com', message.as_string())
            print(f"Reminder sent for {task.name}")
