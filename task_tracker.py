#!/usr/bin/env python3

import sys
from utils import *

def main():
    if len(sys.argv) < 3:
        print("Usage: task-cli <command> [options]")
        print("add ""task name"" - Add a new task")
        print("update <task_id> ""new task name"" - Update a task")
        print("delete <task_id> - Delete a task")
        print("mark-done <task_id> - Mark a task as done")
        print("mark-onGoing <task_id> - Mark a task as on-going")
        print("list - List all tasks")
        print("list done - List all done tasks")
        print("list not done - List all not done tasks")
        print("list on-going - List all on-going tasks")
        print("list <task_id> - List a specific task")
        return
    
    print(sys.argv[1])
        
    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])
    elif command == "update":
        update_task(sys.argv[2],sys.argv[3])
    elif command == "delete":
        delete_task(sys.argv[2])
    elif command == "list":
        list_tasks()
    elif command == "mark-done":
        mark_done(sys.argv[2])
    elif command == "mark-onGoing":
        mark_onGoing(sys.argv[2])
    else:   
        print(f"Unknown command: {command}")



if __name__ == "__main__":
    main()
