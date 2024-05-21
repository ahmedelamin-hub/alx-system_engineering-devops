#!/usr/bin/python3
"""
Python script that fetches the TODO list progres
"""

import json
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

    # Get the employee username
    username = user_data.get("username")

    # Create the list of tasks
    tasks = []
    for todo in todos_data:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks.append(task)

    # Create the data dictionary
    data = {employee_id: tasks}

    # Define the JSON file name
    json_file = "{}.json".format(employee_id)

    # Write to the JSON file
    with open(json_file, mode='w') as file:
        json.dump(data, file)
