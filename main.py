import json
import datetime

e =  datetime.datetime.now()
tasks = {}

def save_to_file():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task_id, description, status):
    tasks[f"task{task_id}"] = {
        "id": task_id,
        "Description": description,
        "Status": status,
        "createdAt": f"{e}",
        "updatedAt": ""
    }
    save_to_file() 
    # end of function

def delete_task(task_id):
    del tasks[f"task{task_id}"]
    save_to_file() 
    # end of function

def update_task(task_id, description):
    date = datetime.datetime.now()
    tasks[f"task{task_id}"].update({"Description": description})
    tasks[f"task{task_id}"].update({"updatedAt": f"{date}"})
    save_to_file() 
    # end of function

def mark_in_progress(task_id):
    date = datetime.datetime.now()
    tasks[f"task{task_id}"].update({"Status": "in-progress"})
    tasks[f"task{task_id}"].update({"updatedAt": f"{date}"})
    save_to_file() 
    # end of function
def mark_done(task_id):
    date = datetime.datetime.now()
    tasks[f"task{task_id}"].update({"Status": "done"})
    tasks[f"task{task_id}"].update({"updatedAt": f"{date}"})
    save_to_file()
    # end of function
def mark_todo(task_id):
    date = datetime.datetime.now()
    tasks[f"task{task_id}"].update({"Status": "todo"})
    tasks[f"task{task_id}"].update({"updatedAt": f"{date}"})
    save_to_file()
    # end of function
def list_tasks():
    print(json.dumps(tasks, indent=3))
    # end of function

def list_done_tasks():
    for key, val in tasks.items():
        if val["Status"] == "done":
            print(key, ':', val)
    # end of function

def list_todo():
    for key, val in tasks.items():
        if val["Status"] == "todo":
            print(key, ':', val)
    # end of function

def list_in_progress():
    for key, val in tasks.items():
        if val["Status"] == "in-progress":
            print(key, ':', val)
    # end of function

# add_task(1, "Go to the mall", "in-progress")
# add_task(2, "Eat at the mall", "done")
# add_task(3,"Go Home","todo")
print(tasks)
#update_task(2, "Going to the gym")
#update_task(1, "Eating healthy food")
