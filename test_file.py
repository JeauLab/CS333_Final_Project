import unittest
from schedule import Schedule
from task import Task

class TestCases(unittest.TestCase):
    def test_add(self):
        t = Task()
        self.assertEqual(t.add(5), 6)

    def test_sub(self):
        t = Task()
        self.assertEqual(t.sub(5), 4)

if __name__ == "__main__":
    unittest.main()
