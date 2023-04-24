from date import Date
import datetime

# Function to translate month value to days
def month_to_days(month_num):
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        days = 0
        index = int(month_num) - 2
        if index >= 0:
            while index >= 0:
                days = days + days_in_month[index]
                index = index - 1
        return days

class Task():
    def __init__(self, task_name):
        # Name of the given task
        self.name = task_name
        # Importance level of the task
        self.importance = 0
        # Date of the task
        self.date = Date()
        # Days until task
        self.days_left = 0
        # Importance/Day Ratio
        self.IDR = 0
    
    # Method to set the name of the task
    def set_name(self, task_name):
        self.name = task_name
    
    # Method to set the importance level of the task
    def set_importance(self, importance_level):
        self.importance = importance_level
    
    # Method to set the date the task needs to be done
    def set_date(self, date):
        self.date.set_equal(date)
        self.calculate_days_left()
    
    # Method to set this task to be equal to another
    def set_equal(self, other_task):
        self.name = other_task.name
        self.importance = other_task.importance
        self.date.set_equal(other_task.date)
        self.days_left = other_task.days_left
        self.IDR = other_task.IDR

    # Method to calculate numbers of days left until task
    def calculate_days_left(self):
        days_left = 0
        date1_total = 0
        date2_total = 0
        today = Date()
        today.set_today()
        date1_total = month_to_days(today.month) + int(today.day) + (int(today.year))*365
        date2_total = month_to_days(self.date.month) + int(self.date.day) + (int(self.date.year))*365
        self.days_left = date2_total-date1_total
        self.calculate_IDR()
    
    # Method to calculate the importance to date ratio
    # Importance to date ratio is used for one method of sorting
    def calculate_IDR(self):
        self.IDR = float(self.importance)/float(self.days_left)

    


        

    
