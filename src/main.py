import os
import task_manager as tm

while True:
    cmd = input("task-cli > ").split(" ")
    if cmd[0].lower() == "help": tm.help()
    elif cmd[0].lower() == "exit": break

    elif cmd.[0].lower()

    else:
        tm.help()