#!/usr/bin/python3
"""
This Python script retrieves and displays the TODO list progress of a given
employee based on their employee ID using a REST API. The script uses the requests
module to fetch data and displays the progress in a specified format.
"""

import requests
import json

def fetch_all_employees_todo():
    # Base URLs for the API
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        # Fetch all employees information
        users_response = requests.get(users_url)
        users_response.raise_for_status()
        users_data = users_response.json()

        # Fetch all TODO lists
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Create a dictionary to hold the JSON data
        json_data = {}

        for user in users_data:
            user_id = user.get("id")
            username = user.get("name")
            user_todos = [task for task in todos_data if task.get("userId") == user_id]

            json_data[str(user_id)] = [
                {"username": username, "task": task.get("title"), "completed": task.get("completed")}
                for task in user_todos
            ]

        # Export data to JSON
        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as file:
            json.dump(json_data, file, indent=4)

        print(f"Data exported to {json_filename}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    fetch_all_employees_todo()
