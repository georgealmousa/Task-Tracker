package main

type Task struct {
    ID int 
    description string
    status []string
    createdAt string
    updatedAt string
}

func listTask(task Task )string{
    return task.description + " ==> " + task.status[0]  ;
}