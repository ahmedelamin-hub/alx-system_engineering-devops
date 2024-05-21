#!/usr/bin/python3
"""
Python script that fetches the TODO list progress for a given employee ID
using the JSONPlaceholder REST API and exports it to a CSV file.
"""

import csv
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

    # Define the CSV file name
    csv_file = "{}.csv".format(employee_id)

    # Write to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([employee_id, username, todo.get("completed"), todo.get("title")])
