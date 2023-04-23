import unittest
from schedule import Schedule
from task import Task
from date import Date
from datetime import date

class TestCases(unittest.TestCase):
    def test_date_init(self):
        d = Date()
        self.assertEqual(0, d.month)
        self.assertEqual(0, d.day)
        self.assertEqual(0, d.year)

    def test_set_month(self):
        d = Date()
        d.set_month(7)
        self.assertEqual(d.month, 7)

    def test_set_day(self):
        d = Date()
        d.set_day(11)
        self.assertEqual(d.day, 11)
    
    def test_set_year(self):
        d = Date()
        d.set_year(2001)
        self.assertEqual(d.year, 2001)
    
    def test_get_year(self):
        d = Date()
        d.set_year(2001)
        self.assertEqual(d.get_year(), 2001)

    def test_set_get_date_MDY(self):
        d = Date()
        date = [7,11,2001]
        d.set_date_MDY(7,11,2001)
        self.assertEqual(date, d.get_date_MDY())
    
    def test_set_today(self):
        d = Date()
        d.set_today()
        today = date.today()
        date_string = today.strftime('%Y-%m-%d')
        parts = date_string.split("-")
        self.assertEqual(parts[0], d.year)
        self.assertEqual(parts[1], d.month)
        self.assertEqual(parts[2], d.day)
        
        



if __name__ == "__main__":
    unittest.main()
