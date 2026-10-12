#!/usr/bin/python3
"""Export all employees' TODO lists to a JSON file."""
import json
import urllib.request


if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    with urllib.request.urlopen("{}/users".format(base)) as response:
        users = json.loads(response.read().decode("utf-8"))
    with urllib.request.urlopen("{}/todos".format(base)) as response:
        todos = json.loads(response.read().decode("utf-8"))
    data = {}
    for user in users:
        uid = str(user.get("id"))
        data[uid] = [{"username": user.get("username"),
                      "task": task.get("title"),
                      "completed": task.get("completed")}
                     for task in todos
                     if task.get("userId") == user.get("id")]
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
