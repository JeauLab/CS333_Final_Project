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

    # Function to sort list by importance
    def sort_by_importance(self):
        for i in range(len(self.task_list)):
           for j in range(len(self.task_list)):
               if self.task_list[i].importance > self.task_list[j].importance:
                   temp = Task("")
                   temp.set_equal(self.task_list[i])
                   self.task_list[i].set_equal(self.task_list[j])
                   self.task_list[j].set_equal(temp)

    # Function to sort list by date due
    def sort_by_date(self):
        for i in range(len(self.task_list)):
           for j in range(len(self.task_list)):
               if self.task_list[i].days_left < self.task_list[j].days_left:
                   temp = Task("")
                   temp.set_equal(self.task_list[i])
                   self.task_list[i].set_equal(self.task_list[j])
                   self.task_list[j].set_equal(temp)

    # Function to sort list by IDR
    def sort_by_IDR(self):
        for i in range(len(self.task_list)):
           for j in range(len(self.task_list)):
               if self.task_list[i].IDR > self.task_list[j].IDR:
                   temp = Task("")
                   temp.set_equal(self.task_list[i])
                   self.task_list[i].set_equal(self.task_list[j])
                   self.task_list[j].set_equal(temp)