#!/usr/bin/python3
"""
Python script that fetches the TODO list progress for a given employee ID
using the JSONPlaceholder REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch todo data
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Get the employee name
    employee_name = user_data.get("name")

    # Filter completed tasks
    completed_tasks = [todo for todo in todos_data if todo.get("completed")]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    # Print the result
    print("Employee {} is done with tasks({}/{}):".format(employee_name, number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
