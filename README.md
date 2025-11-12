# Task-Tracker-CLI

## To initiate:
```bash
python main.py
task-cli > function
```

There's a help function which shows all functions and parameters needed for each
In case you don´t use an existing function it will call help function
If you call a correct function but don't use correct parameters it will show you a message showing the correct use of that function

Functions available:
- help
- exit

- add <task description>
- update <task ID> <new task description>
- delete <task ID>
- list [done/todo/in-progress]

- mark-in-progress <task ID>
- mark-done <task ID>

Example of use:
```bash
python main.py
help
exit
add do homework
update 1 do chores
delete 1
list
list done
mark-in-progress 1
mark-done 1
```