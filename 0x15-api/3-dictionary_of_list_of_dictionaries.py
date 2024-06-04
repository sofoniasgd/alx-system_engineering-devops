#!/usr/bin/python3
"""3. Dictionary of list of dictionaries
exports employee tasks data for all employees"""


import json
import requests

if __name__ == "__main__":
    """ export data in the JSON format for every employee
    export format:
    { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    """
    url = "https://jsonplaceholder.typicode.com/"

    # get todos json for tasks list
    task_list = requests.get(url + "todos").json()

    user_dictionary = {}
    user_tasks = []
    task_dict = {}
    tasks_total = 0

    for task in task_list:
        user_id = task["userId"]
        # if new user_id create dictionary entry
        if task['userId'] not in user_dictionary.keys():
            user_dictionary[user_id] = []

        task_dict = {}
        # get username
        user = requests.get(url + "users/" + str(user_id)).json()["username"]
        task_dict["task"] = task['title']
        task_dict["completed"] = task['completed']
        task_dict["username"] = user

        # add dict to the right list
        task_list = user_dictionary[user_id]
        task_list.append(task_dict)

    # write json
    with open("todo_all_employees.json", "w") as file:
        json.dump(user_dictionary, file)
