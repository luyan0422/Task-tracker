#!/usr/bin/env python

import sys
import json
import os

TASK_FILE = "tasks.json"

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        print("---commands---")
        print("add : add task")
        return
    
    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])
    elif command == "update":
        update_task(sys.argv[2])
    elif command == "delete":
        delete_task(sys.argv[2])
    elif command == "list":
        list_tasks()
    else:
        print(f"Unknown command: {command}")

def add_task(args):
    if len(args) < 1:
        print("Usage: task-cli add <task_name>")
        return

    task_name = " ".join(args)
    task = {
        "id": generate_task_id(),
        "name": task_name,
        "status": "not done"
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {task['id']}).")

def update_task(args):
    if len(args) < 2:
        print("Usage: task-cli update <task_id> <new_task_name>")
        return

    task_id = int(args[0])
    new_name = " ".join(args[1:])
    
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) updated successfully.")
            return

    print(f"Task (ID: {task_id}) not found.")

def delete_task(args):
    if len(args) < 1:
        print("Usage: task-cli delete <task_id>")
        return

    task_id = int(args[0])
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task (ID: {task_id}) deleted successfully.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"ID: {task['id']} - {task['name']} [{task['status']}]")

def generate_task_id():
    tasks = load_tasks()
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

if __name__ == "__main__":
    main()
