#!/usr/bin/python3
"""1. Export to CSV
exports employee tasks data"""


import requests
import sys

if __name__ == "__main__":
    """ Records all tasks that are owned by this employee
    export format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
    """
    url = "https://jsonplaceholder.typicode.com/"
    e_id = sys.argv[1]

    user_name = requests.get(url + "users/" + e_id).json()["username"]

    # get todos json for tasks list
    tasks_list = []
    tasks_total = 0
    todo = requests.get(url + "todos").json()
    for task in todo:
        if task['userId'] == int(e_id):
            tasks_total += 1
            line = []
            line += [e_id, user_name, str(task["completed"]), task["title"]]
            # list to comma separated strings with quotes
            string = ','.join(f'"{i}"' for i in line)
            string += "\n"
            tasks_list.append(string)

    # write CSV
    with open(e_id + ".csv", "w") as file:

        for line in tasks_list:
            file.write(line)
