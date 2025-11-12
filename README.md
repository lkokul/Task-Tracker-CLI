# Task-Tracker-CLI

A simple command-line tool to manage tasks directly from the terminal.

> This project was built following the [Task Tracker project guide on roadmap.sh](https://roadmap.sh/projects/task-tracker).
---

## How to Run

```bash
python main.py
````

Once running, the prompt will appear as:

```
task-cli >
```

You can then type any of the following commands.

---

> [!Notes]

> Use the `help` command to display all available functions and their parameters.  
> If you call a **non-existing function**, the program automatically shows the help message.  
> If you call a **valid function** but use **incorrect parameters**, the CLI will display the correct usage.  

---

## Available Commands

| Command                              | Description                            |
| ------------------------------------ | -------------------------------------- |
| `help`                               | Show all commands and usage info       |
| `exit`                               | Exit the CLI                           |
| `add <task description>`             | Add a new task                         |
| `update <task ID> <new description>` | Update an existing task                |
| `delete <task ID>`                   | Delete a task by ID                    |
| `list [done/todo/in-progress]`       | List all tasks (or filtered by status) |
| `mark-in-progress <task ID>`         | Mark a task as in progress             |
| `mark-done <task ID>`                | Mark a task as done                    |

---

## Examples

```bash
python main.py
```

Then inside the prompt:

```
task-cli > help
task-cli > add do homework
task-cli > update 1 do chores
task-cli > delete 1
task-cli > list
task-cli > list done
task-cli > mark-in-progress 1
task-cli > mark-done 1
task-cli > exit
```

---

## Notes for Developers

* The CLI automatically validates command parameters.
* Data is stored in a local JSON file (`task_register.json`).
* Each task contains:

  * `id` — numeric unique identifier
  * `description`
  * `status` (`todo`, `in-progress`, or `done`)
  * `createdAt` and `updatedAt` timestamps

```