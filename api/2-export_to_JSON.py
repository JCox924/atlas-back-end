import requests
import sys
import csv
import json


def get_employee_todo_progress(employee_id):
    # Base URLs for the API
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Fetch employee information
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        # Fetch employee TODO list
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Extract employee name
        employee_name = user_data.get("name")

        # Count the number of completed and total tasks
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]
        number_of_done_tasks = len(done_tasks)

        # Display the TODO list progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

        for task in done_tasks:
            print(f"\t {task.get('title')}")

        # Export data to CSV
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todos_data:
                writer.writerow([employee_id, employee_name, task.get("completed"), task.get("title")])

        print(f"Data exported to {csv_filename}")

        # Export data to JSON
        json_filename = f"{employee_id}.json"
        json_data = {
            str(employee_id): [
                {"task": task.get("title"), "completed": task.get("completed"), "username": employee_name}
                for task in todos_data
            ]
        }
        with open(json_filename, mode='w') as file:
            json.dump(json_data, file, indent=4)

        print(f"Data exported to {json_filename}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)
