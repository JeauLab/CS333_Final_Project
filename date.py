from datetime import date
class Date():
    def __init__(self):
        self.month = 0
        self.day = 0
        self.year = 0
    
    def set_month(self, m):
        self.month = m
        return

    def set_day(self, d):
        self.day = d
        return
    
    def set_year(self, y):
        self.year = y
        return

    def set_date_MDY(self, m, d, y):
        self.month = m
        self.day = d
        self.year = y

    def set_today(self):
        today = date.today()
        date_string = today.strftime('%Y-%m-%d')
        parts = date_string.split("-")
        self.year = parts[0]
        self.month = parts[1]
        self.day = parts[2]

