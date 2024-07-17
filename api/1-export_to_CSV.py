#!/usr/bin/python3
"""Script that exports tasks owned by an employee to a CSV file"""
import csv
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

    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([employee_id, username,
                             todo['completed'], todo['title']])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
