import unittest
from schedule import Schedule
from task import Task
from date import Date
from datetime import date

class TestCases(unittest.TestCase):

    # DATE UNIT TESTS

    # Date Unit Test
    def test_date_init(self):
        d = Date()
        self.assertEqual(0, d.month)
        self.assertEqual(0, d.day)
        self.assertEqual(0, d.year)

    # Date Unit Test
    def test_set_month(self):
        d = Date()
        d.set_month(7)
        self.assertEqual(d.month, 7)

    # Date Unit Test
    def test_set_day(self):
        d = Date()
        d.set_day(11)
        self.assertEqual(d.day, 11)
    
    # Date Unit Test
    def test_set_year(self):
        d = Date()
        d.set_year(2001)
        self.assertEqual(d.year, 2001)
    
    # Date Unit Test
    def test_equals(self):
        d = Date()
        i = Date()
        i.set_date_MDY(7,11,2001)
        d.set_equal(i)
        self.assertEqual(d.month, i.month)
        self.assertEqual(d.day, i.day)
        self.assertEqual(d.year, i.year)

    # Date Unit Test
    def test_set_get_date_MDY(self):
        d = Date()
        d.set_date_MDY(7,11,2001)
        self.assertEqual(7, d.month)
        self.assertEqual(11, d.day)
        self.assertEqual(2001, d.year)
    
    # Date Unit Test
    def test_set_today(self):
        d = Date()
        d.set_today()
        today = date.today()
        date_string = today.strftime('%Y-%m-%d')
        parts = date_string.split("-")
        self.assertEqual(parts[0], d.year)
        self.assertEqual(parts[1], d.month)
        self.assertEqual(parts[2], d.day)

    # TASK UNIT AND INTEGRATION TESTS
    
    # Task Unit Test (Integration Test with Date)
    def test_task_create(self):
        t = Task("Laundry")
        self.assertEqual(t.name, "Laundry")
        self.assertEqual(t.importance, 0)
        self.assertEqual(t.date.month, 0)
        self.assertEqual(t.date.day, 0)
        self.assertEqual(t.date.year, 0)
    
    # Task Unit Test 
    def test_set_name(self):
        t = Task("")
        t.set_name("Get Gas")
        self.assertEqual(t.name, "Get Gas")
    
    # Task Unit Test 
    def test_set_importance(self):
        t = Task("")
        t.set_importance(10)
        self.assertEqual(t.importance, 10)
    
    # Task Unit Test (Integration Test with Date)
    def test_set_date(self):
        t = Task("")
        d = Date()
        d.set_date_MDY(7,11,2001)
        t.set_date(d)
        self.assertEqual(t.date.month, 7)
        self.assertEqual(t.date.day, 11)
        self.assertEqual(t.date.year, 2001)
    
    # Task Unit Test (Integration Test with Date)
    def test_calculate_days_left(self):
        t = Task("")
        t.date.set_date_MDY(7,11,2023)
        t.calculate_days_left()
        self.assertGreater(t.days_left, 0)
    
    # Task Unit Test
    def test_calculate_IDR(self):
        t = Task("")
        t.set_importance(10)
        t.days_left = 2
        t.calculate_IDR()
        self.assertEqual(t.IDR, 5)

    # SCHEDULE UNIT AND INTEGRATION TESTS

    # Schedule Unit Test
    def test_schedule(self):
        s = Schedule()
        self.assertListEqual(s.task_list, [])

    # Schedule Unit Test (Integration Test with Task)
    def test_add_task(self):
        s = Schedule()
        t = Task("Laundry")
        list = []
        list.append(t)
        s.add_task(t)
        self.assertListEqual(s.task_list, list)

    # Schedule Unit Test (Integration Test with Task)
    def test_remove_task(self):
        s = Schedule()
        t = Task("Laundry")
        j = Task("Homework")
        list = []
        list.append(j)
        s.add_task(t)
        s.add_task(j)
        s.remove_task(t)
        self.assertListEqual(s.task_list, list)

    # Schedule Unit Test (Integration Test with Task)
    def test_clear_list(self):
        s = Schedule()
        t = Task("Laundry")
        list = []
        s.add_task(t)
        s.clear_list()
        self.assertListEqual(s.task_list, list)
    
    # Schedule Unit Test (Integration Test with Task)
    def test_find_task_index(self):
        s = Schedule()
        t = Task("Laundry")
        j = Task("Homework")
        s.add_task(t)
        s.add_task(j)
        self.assertEqual(s.find_task_index(j), 1)


if __name__ == "__main__":
    unittest.main()
