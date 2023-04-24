from datetime import date
class Date():
    # Initialize date to be empty on creation
    def __init__(self):
        self.month = 0
        self.day = 0
        self.year = 0
    
    # Simple setter function for month
    def set_month(self, m):
        self.month = m
        return

    # Simple setter function for day
    def set_day(self, d):
        self.day = d
        return
    
    # Simple setter function for year
    def set_year(self, y):
        self.year = y
        return

    # Set all three at the same time
    def set_date_MDY(self, m, d, y):
        self.month = m
        self.day = d
        self.year = y
    
    # Equality function to set two dates equal to one another
    def set_equal(self, other_date):
        self.month = other_date.month
        self.day = other_date.day
        self.year = other_date.year

    # Function to set the current date equal to that of today
    def set_today(self):
        today = date.today()
        date_string = today.strftime('%Y-%m-%d')
        parts = date_string.split("-")
        self.year = parts[0]
        self.month = parts[1]
        self.day = parts[2]

