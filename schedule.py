from task import Task

class Schedule():
    def __init__(self):
        # Main list where tasks will be sorted
        self.task_list = []

    # Add a task to the main list
    def add_task(self, task):
        self.task_list.append(task)
        return

    # Remove given task from the main list
    def remove_task(self, task):
        index = self.find_task_index(task)
        self.task_list.pop(index)

    # Clear the entire list
    def clear_list(self):
        self.task_list = []
    
    # Traverse the list and return the index of the desired task
    # Main use is getting index for remove function
    def find_task_index(self, task):
        for i in range(len(self.task_list)):
            if self.task_list[i].name == task.name:
                return i
    
    # No unit testing here officer just some I/O
    def display_schedule(self):
        print("\n ID |  Task  | Importance |  Days Till  |     Due     |    I/D Ratio")
        print("---------------------------------------------------------------")
        i = 0
        for task in self.task_list:
            print(i," ", task.name, "     ",task.importance, 
            "        ",task.days_left, "      ", task.date.month, 
            "-", task.date.day, "-", task.date.year, "    ", round(task.IDR,2))
            i += 1