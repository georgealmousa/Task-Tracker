# Task CLI Application

This project provides a command-line interface (CLI) application to manage tasks. The application supports the following operations:

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List tasks by status (done, todo, in-progress)

## Requirements

- Use positional arguments for user inputs.
- Store tasks in a JSON file in the current directory.
- Handle the creation of the JSON file if it does not exist.
- Use native file system modules.
- Do not use external libraries or frameworks.
- Handle errors and edge cases gracefully.

## Commands and Usage

### Adding a New Task
```bash
task-cli add "Buy groceries"
```
**Output:**
```
Task added successfully (ID: 1)
```

### Updating and Deleting Tasks
- Update a task:
```bash
task-cli update 1 "Buy groceries and cook dinner"
```

- Delete a task:
```bash
task-cli delete 1
```

### Marking a Task
- Mark a task as in progress:
```bash
task-cli mark-in-progress 1
```

- Mark a task as done:
```bash
task-cli mark-done 1
```

### Listing Tasks
- List all tasks:
```bash
task-cli list
```

- List tasks by status:
  - Done:
    ```bash
    task-cli list done
    ```
  - Todo:
    ```bash
    task-cli list todo
    ```
  - In progress:
    ```bash
    task-cli list in-progress
    ```

## Task Properties

Each task includes the following properties:

- `id`: A unique identifier for the task.
- `description`: A short description of the task.
- `status`: The status of the task (`todo`, `in-progress`, `done`).
- `createdAt`: The date and time when the task was created.
- `updatedAt`: The date and time when the task was last updated.

## Implementation Details

### JSON File Handling
- The application uses a JSON file to store tasks.
- The JSON file is created automatically if it does not exist.
- Tasks are stored as an array of objects in the JSON file.

### Error Handling
- Handle invalid commands and arguments gracefully.
- Ensure unique task IDs.
- Validate task IDs before performing operations (update, delete, mark).

### Example JSON Structure
```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2025-01-16T10:00:00Z",
        "updatedAt": "2025-01-16T10:00:00Z"
    },
    {
        "id": 2,
        "description": "Prepare for meeting",
        "status": "in-progress",
        "createdAt": "2025-01-16T11:00:00Z",
        "updatedAt": "2025-01-16T11:30:00Z"
    }
]
```

## Constraints

- Use any programming language of your choice.
- Avoid external libraries or frameworks.
- Implement using native file system operations.
- Provide meaningful feedback to the user for all commands and operations.
