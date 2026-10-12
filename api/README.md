# API

Python scripts that consume the [JSONPlaceholder](https://jsonplaceholder.typicode.com)
REST API to gather employee TODO data and export it to CSV and JSON.

| File | Description |
|---|---|
| `0-gather_data_from_an_API.py` | Prints an employee's TODO progress (`done/total`) and each completed task title |
| `1-export_to_CSV.py` | Exports all of an employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports all of an employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports every employee's tasks to `todo_all_employees.json` |

## Usage

```bash
./0-gather_data_from_an_API.py 2
./1-export_to_CSV.py 2
./2-export_to_JSON.py 2
./3-dictionary_of_list_of_dictionaries.py
```

The scripts use only the Python standard library (`urllib.request`, `json`, `csv`).
