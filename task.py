from date import Date
class Task():
    def __init__(self, task_name):
        # Name of the given task
        self.name = task_name

        # Importance level of the task
        self.importance = 0

        # Date of the task
        self.date = Date()
    
    def set_name(self, task_name):
        self.name = task_name
    
    def set_importance(self, importance_level):
        self.importance = importance_level
    
    def set_date(self, date):
        self.date.set_equal(date)
