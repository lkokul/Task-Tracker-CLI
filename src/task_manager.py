import json, os
from datetime import datetime

def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as e:
                print(e)

        return wrapper

class TaskManager:
    file_name = "task_register.json"
    def __init__(self, description=None):
        self.id = self.get_id()
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now()
        self.updatedAt= None

        task = {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": str(self.createdAt),
            "updatedAt": str(self.updatedAt)
        }

        # Since it's used file.write it's needed to use a string (dumps turns a dicc into a str)
        # It could be uploaded to just using dump(dicctionary)
        # json.dump(task, file, ident)
        try:
            contents = self.read_file()


        except (FileNotFoundError, json.JSONDecodeError):
            contents = []

        contents.append(task)
        self.write_file(contents)
        print(f'Task added successfully (ID:{task["id"]})')

    @staticmethod
    def get_id():
        """This function is used to save and remember the last id, so it doesn't repeat it"""
        if not os.path.exists(TaskManager.file_name):
            return 1

        try:
            contents = TaskManager.read_file()
            if contents: return max(cont["id"] for cont in contents) + 1
        
        except (json.JSONDecodeError, KeyError): pass
        return 1

    @classmethod
    @decorator
    def help(cls):
        """Shows the available methods and how to use them"""
        print('''
            - help
            - exit

            - add <task description>
            - update <task ID> <new task description>
            - delete <task ID>
            - list [done/todo/in-progress]
            
            - mark-in-progress <task ID>
            - mark-done <task ID>
            ''')

    @classmethod
    def read_file(cls):
        with open(TaskManager.file_name, "r") as file:
            return json.load(file)

    @classmethod
    def write_file(cls, contents):
        with open(TaskManager.file_name, "w") as file:
            json.dump(contents, file, indent=2)

    @classmethod
    @decorator
    def update_task(cls, update_task):
        """
        Updates a task description
        Is made as a classmethod because we don't use an especific object, we just use the class
        """
        task_id = int(update_task.get("task_id"))
        description = update_task.get("description")

        contents = TaskManager.read_file()

        for cont in contents:
            if cont["id"] == task_id:
                cont["description"] = description
                cont["updatedAt"] = str(datetime.now())
                print(f'Task updated successfully (ID:{cont["id"]})')

        TaskManager.write_file(contents)

    @classmethod
    @decorator
    def delete_task(cls, del_task):
        """
        Deletes a task
        Is made as a classmethod because we don't use an especific object, we just use the class
        """
        contents = TaskManager.read_file()

        print(f'Task deleted successfully (ID:{cont["id"]})')           
        contents = [cont for cont in contents if cont["id"] != int(del_task)]

        TaskManager.write_file(contents)

    @classmethod
    @decorator
    def mark_a_task(cls, task):
        """
        Marks a task as done or in-progress, the status may coincide with the filter status of the next function
        In order to be able to correctly filter the tasks
        """
        task_id = task.get("task_id")
        status = task.get("status")
        contents = TaskManager.read_file()

        for cont in contents:
            if cont["id"] == int(task_id):
                cont["status"] = status
                cont["updatedAt"] = str(datetime.now())
                print(f'Task updated successfully (ID:{cont["id"]})')

        TaskManager.write_file(contents)

    @classmethod
    @decorator
    def list_tasks(cls, filter_status=None):
        """List taks, if it takes a filer, only shows that status, else it shows all the tasks"""
        contents = TaskManager.read_file()
        for cont in contents:
            if filter_status and cont["status"] == filter_status:
                print(cont)
            elif not filter_status: print(cont)