from task import Task
from date import Date

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

    # Function to read data from a file
    # File IO No Unit Testing Here
    def load_data(self):
        file = open("save_data", 'r')
        # Read the contents of the file
        file_contents = file.readlines()
        # For each line in the file
        # Each line corresponds to one task
        for line in file_contents:
            # Temp task as a placeholder
            temp_task = Task("")

            # Split operator to differentiate data
            parts = line.split("|")

            # Assigning data
            temp_task.set_name(parts[0])
            temp_task.set_importance(int(parts[1]))
            temp_task.days_left = int(parts[2])
            date_parts = parts[3].split("-")
            temp_date = Date()
            temp_date.set_date_MDY(int(date_parts[0]),int(date_parts[1]),int(date_parts[2]))
            temp_task.set_date(temp_date)
            temp_task.IDR = float(parts[4])

            self.task_list.append(temp_task)


        # Close the file
        file.close()
        
    
    # Function to save data to a file
    # File IO No Unit Testing Here
    def save_data(self):
        file = open("save_data", 'w')
        for task in self.task_list:
            writable = str(task.name)+"|"+str(task.importance)+"|"+str(task.days_left)+"|"+str(task.date.month)+"-"+str(task.date.day)+"-"+str(task.date.year)+"|"+str(task.IDR)+"\n"
            file.write(writable)
        # Close the file
        file.close()


