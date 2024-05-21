#!/usr/bin/python3
"""
Python script that fetches the TODO list progress for all employees
REST API and exports it to a JSON file.
"""

import json
import requests


if __name__ == "__main__":
    # Fetch all users data
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to store all tasks by user
    all_tasks = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch todo data for each user
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # List to store tasks for the current user
        tasks = []
        for todo in todos_data:
            task = {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            tasks.append(task)

        # Add the user's tasks to the dictionary
        all_tasks[user_id] = tasks

    # Define the JSON file name
    json_file = "todo_all_employees.json"

    # Write to the JSON file
    with open(json_file, mode='w') as file:
        json.dump(all_tasks, file)
