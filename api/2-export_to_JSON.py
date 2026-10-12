#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    emp_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users/{}".format(base, emp_id)
    todos_url = "{}/todos?userId={}".format(base, emp_id)
    with urllib.request.urlopen(users_url) as response:
        user = json.loads(response.read().decode("utf-8"))
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))
    username = user.get("username")
    data = {emp_id: [{"task": task.get("title"),
                      "completed": task.get("completed"),
                      "username": username} for task in todos]}
    with open("{}.json".format(emp_id), "w") as jsonfile:
        json.dump(data, jsonfile)
