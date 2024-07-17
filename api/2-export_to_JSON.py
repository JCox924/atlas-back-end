#!/usr/bin/python3
"""Script that exports data in the JSON format"""
import json
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """Fetches the employee's todo list progress"""
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    employee_data = requests.get(employee_url).json()
    username = employee_data.get('username')

    todos_response = requests.get(
        "{}/todos".format(base_url), params={'userId': employee_id}
    )
    todos_data = todos_response.json()

    data = [{
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
            } for todo in todos_data]

    format = {str(employee_id): data}

    file = f"{employee_id}.json"
    with open(file, 'w') as f:
        json.dump(format, f)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
