#!/usr/bin/python3
"""Fetch an employee's TODO progress from the JSONPlaceholder API."""
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
    done = [task for task in todos if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
