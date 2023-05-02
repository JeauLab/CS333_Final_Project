from task import Task
from date import Date
from datetime import date
from schedule import Schedule

def main():
    main_schedule = Schedule()
    while True:
        print("\n      Task Scheduler      ")
        print("==========================")
        print("1.     View Schedule      ")
        print("2.       Add Task         ")
        print("3.      Remove Task       ")
        print("4.     Sort Schedule      ")
        print("5.     Clear Schedule     ")
        print("6.     Load From File     ")
        print("7.      Save To File      ")
        print("0.         Exit           ")
        choice = input(">>")
        
        # User wants to view the schedule
        if choice == "1":
            main_schedule.display_schedule()
            if len(main_schedule.task_list) == 0:
                print("                       SCHEDULE EMPTY                       ")

        # User wants to add a task to the schedule
        elif choice == "2":
            # Open up a sub menu for task creation
            print("\n       New Task       ")
            print("----------------------")
            new_name = input("Task Name: ")
            new_importance = input("Task Importance (1-10): ")
            new_date = input("Complete Task By (MM-DD-YYYY): ")
            
            # Date shenanigans 
            temp_date = Date()
            date_split = new_date.split("-")
            temp_date.set_date_MDY(date_split[0], date_split[1], date_split[2])
            
            # Load that data into a new task object
            task = Task(new_name)
            task.set_importance(new_importance)
            task.set_date(temp_date)

            # Add task object to schedule
            main_schedule.add_task(task)
            print("\nTask Successfully Created!")

        # User wants to remove a task from the schedule
        elif choice == "3":
            exit_val = True
            while exit_val:
                print("\n      Task Removal     ")
                print("-----------------------")
                rm_task = input("Enter Name of Task You Wish to Remove: ")
                for task in main_schedule.task_list:
                    if task.name == rm_task:
                        main_schedule.remove_task(task)
                        print("\nTask Successfully Removed!")
                        exit_val = False
                if exit_val == True:
                    print("Task not found... Please try again.")


        # User wants to use one of the sorting algorithms
        elif choice == "4":
            # Small menu for displaying sorting options to the user
            exit_val = True
            while exit_val:
                print("\n              Schedule Sorter       ")
                print("--------------------------------------")
                print("1.            Sort By Date            ")
                print("2.         Sort By Importance         ")
                print("3.    Sory By Importance/Date Ratio   ")
                print("0.              Main Menu             ")
                sort_choice = input(">>")
                if int(sort_choice) not in [ 0, 1, 2, 3]:
                    print("Please enter one of the choices!")
                else:
                    exit_val = False
            if sort_choice == "1":
                main_schedule.sort_by_date()
                print("\nSchedule sorted by date!")
                main_schedule.display_schedule()
            elif sort_choice == "2":
                main_schedule.sort_by_importance()
                print("\nSchedule sorted by date!")
                main_schedule.display_schedule()
            elif sort_choice == "3":
                main_schedule.sort_by_IDR()
                print("\nSchedule sorted by date!")
                main_schedule.display_schedule()

        # User wants to clear the schedule out
        elif choice == "5":
            main_schedule.clear_list()
            print("\nSchedule Cleared!")
        
        # User wants to load data from a save file
        elif choice == "6":
            main_schedule.load_data()
            print("\nLoaded Save Data Successfully!")
        
        # User wants to save data to file
        elif choice == "7":
            main_schedule.save_data()
            print("\nData Saved Successfully!")

        # Exit the program
        elif choice == "0":
            quit()

        # In case user does not enter one of the choices
        else:
            print("Please enter one of the choices!")
    

if __name__ == '__main__':
    main()
