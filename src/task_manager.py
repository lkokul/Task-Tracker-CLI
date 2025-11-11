import json
from datetime import datetime 

class TaskManager:
    file_name = "task_register.json"
    count = 0
    def __init__(self, description, status):
        self.id = count
        self.description = description
        self.status = status
        self.createdAt = datetime.now()
        self.updatedAt= None

        TaskManager.count += 1

    def decorator(self, function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as e:
                print(e)

        return wrapper

    @classmethod
    @decorator
    def help(cls):
        """Shows the available methods and how to use them"""
        print('''
            - help
            - exit

            - add
            - modify
            - delete
            ''')

    def add_taks(self):
        """Writes a task into task_register file"""
        with open(TaskManager.file_name, "w") as file:
            task = {
                "id": self.id,
                "description": self.description,
                "status": self.status,
                "createdAt": self.createdAt,
                "updatedAt": self.updatedAt
            }
            file.write(json.dump(task)) # We use dump or load to write into an archive or to read it
        print(f'Task added successfully (ID:{task["id"]})')

    def modify_taks(self):
        """Modifies a task from task_register file"""
        with open(file_name, "w") as file:
            file.write(json.dumps(task))

    def delete_taks(self):
        """Deletes a task from task_register file"""
        with open(file_name, "w") as file:
            file.write(json.dumps(task))