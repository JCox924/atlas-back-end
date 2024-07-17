#!/usr/bin/python3
"""Script that exports tasks owned by all employees to a JSON file"""

import json
import requests


def fetch_employee_data(employee_id):
    """Fetches employee data including username"""
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_url)
    return response.json()


def fetch_todo_data(employee_id):
    """Fetches todo data for a given employee ID"""
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(todos_url)
    return response.json()


def export_to_json():
    """Exports tasks for all employees to a JSON file"""
    all_employees_data = {}

    # Assuming there are 10 users as per the example output
    for employee_id in range(1, 11):
        employee_data = fetch_employee_data(employee_id)
        todos_data = fetch_todo_data(employee_id)
        username = employee_data.get('username')

        tasks = [{
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        } for todo in todos_data]

        all_employees_data[str(employee_id)] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_employees_data, file)


if __name__ == "__main__":
    export_to_json()
