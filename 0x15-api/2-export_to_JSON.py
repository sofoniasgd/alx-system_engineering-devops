#!/usr/bin/python3
"""2. Export to JSON
exports employee tasks data"""


import json
import requests
import sys

if __name__ == "__main__":
    """ export data in the JSON format
    export format:
    { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    """
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    task_list = requests.get(url + "todos").json()

    # get todos json for tasks list
    user_dictionary = {}
    user_tasks = []
    task_dict = {}
    tasks_total = 0
    for task in task_list:
        if task['userId'] == int(user_id):
            task_dict = {}
            # get username
            user = requests.get(url + "users/" + user_id).json()["username"]
            task_dict["task"] = task['title']
            task_dict["completed"] = task['completed']
            task_dict["username"] = user

            # add dict to list
            user_tasks.append(task_dict)
    # final json dict
    user_dictionary[user_id] = user_tasks

    # write json
    with open(user_id + ".json", "w") as file:
        json.dump(user_dictionary, file)
