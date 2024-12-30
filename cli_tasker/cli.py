#!/usr/bin/env python3

import sys
from .utils import *

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "hamburger":
        print("I love U 🍔")
        return
    
    if len(sys.argv) < 2:
        print("Usage: task_tracker <command> [options]")
        print("Commands:")
        print("add ""task name"" - Add a new task")
        print("update <task_id> ""new task name"" - Update a task")
        print("delete <task_id> - Delete a task")
        print("mark <task_id> ""status"" - Mark task a user defined status")
        print("mark-done <task_id> - Mark task as done")
        print("list - List all tasks")
        print("list ""status"" - List all tasks with a specific status")
        return
    
    command = sys.argv[1]

    if command == "add":
        if(len(sys.argv) < 3):
            print("Usage: task-cli add ""task name""")
            return
        add_task(sys.argv[2])
    elif command == "update":
        if(len(sys.argv) < 4):
            print("Usage: task-cli update <task_id> ""new task name""")
            return
        update_task(sys.argv[2],sys.argv[3])
    elif command == "delete":
        if(len(sys.argv) < 3):
            print("Usage: task-cli delete <task_id>")
            return
        delete_task(sys.argv[2])
    elif command == "mark":
        if(len(sys.argv) < 4):
            print("Usage: task-cli mark <task_id> ""status""")
            return
        mark(sys.argv[2],sys.argv[3])
    elif command == "mark-done":
        if(len(sys.argv) < 3):
            print("Usage: task-cli mark-done <task_id>")
            return
        mark_done(sys.argv[2])
    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        elif(len(sys.argv) == 3):
            list_status(sys.argv[2])
        else:
            print("list - List all tasks")
            print("list ""status"" - List all tasks with a specific status")
    else:   
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
