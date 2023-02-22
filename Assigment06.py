# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# mariia,02.20.2023,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #
# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        # noinspection PyBroadException
        try: #Try statement for case the file is not exist
            list_of_rows.clear()  # clear current data
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
            file.close()
            return list_of_rows
        except:
            pass

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """
        row = {"Task": task, "Priority": priority}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def search_data_in_the_list(task, list_of_rows):
        """ Search for a task user wants to remove in list of dictionary rows

                :param task: (string) with name of task:
                :param list_of_rows: (list) list of data:
                :return: (row) of dictionary rows if data is found
                """
        for row in list_of_rows:
            if row["Task"].lower() == task.lower(): return row
            else: return False


    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        if len(list_of_rows)==0:
            print()  # Line for looks
            print("There is no task to remove, task list is empty\n")
        else:
            row = Processor.search_data_in_the_list(task, list_of_rows)
            if not row:
                print()  # Line for looks
                print("The task does not exist in the list\n")
            else:
                list_of_rows.remove(row)
                print()  # Line for looks
                print("The task removed successfully!\n")
        return list_of_rows


    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        print("Data saved successfully!")
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        print()  # Line for looks
        return input("Which option would you like to perform? [1 to 4] - ").strip()

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print() # Line for looks
        print("******* The current tasks ToDo are: *******")
        if len(list_of_rows) == 0:
            print("There is no data in the list, yet")
        else:
            for row in list_of_rows:
                print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        task = input("Please enter the task: ").strip()
        priority = input("Please enter the task priority: ").strip()
        print() # Line for looks
        return task,priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        print()  # Line for looks
        return input("What is the name of task you wish to remove? - ").strip()




# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file( file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user and handle user choice
while True:
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str  == '4':  # Exit Program
        print("Goodbye!")
        exit()  # by exiting loop

    else:
        print("Please choose one of valid options: '1' or '2' or '3' or '4'")
        continue # to show the menu
