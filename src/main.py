import os
from task_manager import TaskManager as tm

def clean_terminal():
    os.system('cls')

clean_terminal()
while True:
    try:
        cmd = input("task-cli > ").split(" ")
        if cmd[0].lower() == "help": tm.help()
        elif cmd[0].lower() in ("exit", "e", "close"): break

        elif cmd[0].lower() == "add":
            description = input("     Description of the task: ")
            status = input("     Status of the task: ")

            task = {
                "description" : description,
                "status" : status
            }
            print(task)
            
            obj_task = tm(description=description, status=status)
            obj_task.add_taks()
        
        elif cmd[0].lower() == "delete":
            task_name = input("     Name of the task to delete: ")

            task = {
                "task_name" : task_name,
                "description" : description,
                "status" : status
            }
            print(task)
            tm.add_taks(task)

        else:
            tm.help()
    
    except Exception as e:
        print(e)

clean_terminal()