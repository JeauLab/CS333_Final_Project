from task import Task
from date import Date
from datetime import date
from schedule import Schedule

def main():
    s = Schedule()
    d = Date()
    l = Task("Birthday")
    d.set_date_MDY(7,11,2023)
    l.set_date(d)
    l.set_importance(711)
    s.add_task(l)
    h = Task("Christmas")
    d.set_date_MDY(12,25,2023)
    h.set_date(d)
    h.set_importance(34)
    s.add_task(h)
    c = Task("Graduation")
    d.set_date_MDY(5,17,2023)
    c.set_date(d)
    c.set_importance(4)
    s.add_task(c)
    s.display_schedule()

    

if __name__ == '__main__':
    main()
