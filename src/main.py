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

        # Adding a new task
        elif cmd[0].lower() == "add":
            if len(cmd) < 2:
                print("Use: add <task description>")
                continue

            description = " ".join(cmd[1:])
            obj_task = tm(description=description)

        # Updating and deleting tasks
        elif cmd[0].lower() == "update":
            if len(cmd) < 3:
                print("Use: update <task ID> <new task description>")
                continue
            
            task_update = {
                "task_id" : cmd[1],
                "description" : " ".join(cmd[2:])
            }
            tm.update_task(task_update)
        
        elif cmd[0].lower() == "delete":
            if len(cmd) != 2:
                print("Use: delete <task ID>")
                continue
            del_task = cmd[1]
            tm.delete_task(del_task)

        # Marking a task as in progress or done        
        elif cmd[0].lower().split("-")[0] == "mark":
            if len(cmd) != 2:
                print("Use: mark-in-progress <task ID>")
                continue
            if cmd[0] not in ["mark-in-progress", "mark-done"]: raise Exception("Invalid task status")
            status = "-".join(cmd[0].lower().split("-")[1:])
            task_status = {
                "status" : status,
                "task_id" : cmd[1]
            }
            tm.mark_a_task(task_status)
        
        # Listing all tasks
        elif cmd[0].lower() == "list":
            filter_status = None
            if len(cmd) == 2:
                if cmd[1] not in ["in-progress", "done", "todo"]: raise Exception("Invalid task status to filter")
                filter_status = cmd[1]
            tm.list_tasks(filter_status)

    except Exception as e:
        print(e)

clean_terminal()