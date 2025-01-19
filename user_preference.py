class UserPreferences:
    def __init__(self):
        self.preferences = {
            "reminder_time": "9:00 AM",  # Default reminder time
            "task_priority": "Medium"
        }

    def get_preference(self, key):
        return self.preferences.get(key)

    def set_preference(self, key, value):
        self.preferences[key] = value
