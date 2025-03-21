import json

tasks = {}
def add_task(task_id, description, status):
    tasks[f"task{task_id}"] = {
        "id": task_id,
        "Description": description,
        "Status": status,
        "createdAt": "Fri 21 Mar 2025 10:30:00 PM +04",
        "updatedAt": "Fri 21 Mar 2025 10:30:30 PM +04"
    }
    # end of function

def delete_task(task_id):
    del tasks[f"task{task_id}"]
    # end of function

def update_task(task_id,description):
    tasks[f"task{task_id}"].update({"Description":description})
    # end of function

def mark_in_progress(task_id):
    tasks[f"task{task_id}"].update({"Status":"in-progress"})
    # end of function
def mark_done(task_id):
    tasks[f"task{task_id}"].update({"Status":"done"})
    # end of function
def list_tasks():
    data = json.dumps(tasks,indent=4)
    print(data)
    #end of function

add_task(1, "Go to the mall","in-progress")
add_task(2,"Eat at the mall","in-progress")
## delete_task(1)
##update_task(1,"Going to the gym")
list_tasks()

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)
