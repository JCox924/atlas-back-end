#!/usr/bin/python3
"""
Using what you did in task 0,
extend your Python script to export data in the JSON format
"""
import json
import requests


def export_all_prog_to_json():
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users"
    todo_url = f"{url}/todos"

    user_data = requests.get(user_url).json()
    user_todo_dict = {}

    for user in user_data:
        user_id = user["id"]
        user_name = user["username"]

        todo_data = requests.get(todo_url, params={"userId": user_id}).json()

        user_todo_list = []
        for task in todo_data:
            task_dict = {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name
            }
            user_todo_list.append(task_dict)

        user_todo_dict[f"{user_id}"] = user_todo_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(user_todo_dict, f, indent=4)


if __name__ == "__main__":
    export_all_prog_to_json()
