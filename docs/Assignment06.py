# --------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KClarke,2.16.2023,Modified code to complete assignment 06
# --------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data as two elements of a dictionary {Task,Priority}
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
        # TODO: Add Code Here!
        list_of_rows.clear()  # clear current data
        try:
            file = open(file_name, "r")
            for line in file:
                l_task, l_priority = line.split(",")
                row = {"Task": l_task.strip(), "Priority": l_priority.strip()}
                list_of_rows.append(row)
            file.close()
            return list_of_rows
        except:
            print("File not found.")

        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """

        # TODO: Add Code Here!
        row = {"Task": task, "Priority": priority}
        list_of_rows.append(row)

        return list_of_rows

    @staticmethod
    def remove_data_from_list(str_key_to_remove, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        bln_item_removed = False
        for row in list_of_rows:
            task, priority = dict(row).values()
            if task == str_key_to_remove:
                print("found!")
                list_of_rows.remove(row)
                bln_item_removed = True

        # Update user on the status
        if bln_item_removed:
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        obj_file = open(file_name, "w")
        for dicRow in list_of_rows:
            obj_file.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        obj_file.close()
        return list_of_rows


# Presentation (Input/Output)  ---------------------------------------------- #
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
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        str_choice = input("Which option would you like to perform?\
         [1 to 4] - ").strip()
        print()  # Add an extra line for looks
        return str_choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        if len(list_of_rows) == 0:
            print("List is empty, carpe diem!")

        else:
            print("******* The current tasks ToDo are: *******")
            for row in list_of_rows:
                print(row["Task"] + " (" + row["Priority"] + ")")

            print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        str_task = input("What is the task? - ").strip()
        str_priority = input("What is the priority? [high|low] - ").strip()
        return str_task, str_priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        # TODO: Add Code Here!
        return input("Which TASK would you like removed? - ")


# Main Body of Script  ------------------------------------------------------ #
# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=file_name_str,
                              list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show data table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice add a Task
    if choice_str == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task,
                                               priority=priority,
                                               list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        strKeyToRemove = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(
            str_key_to_remove=strKeyToRemove, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(
            file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
