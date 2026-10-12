#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""
import csv
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
    with open("{}.csv".format(emp_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([emp_id, username,
                             task.get("completed"), task.get("title")])
