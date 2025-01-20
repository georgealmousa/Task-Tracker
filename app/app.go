package main

import (
	"fmt"
)

func main(){
    task1:=Task{
        ID: 1,
        description: "Learn Go structs",
        status:      []string{"in-progress","done","to-do"},
        createdAt:   "2025-01-20",
        updatedAt:   "2025-01-20",
    }
    fmt.Println(listTask(task1));
}