#!/usr/bin/python3
"""2. Export to JSON
exports employee tasks data"""


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

    task_list = requests.get(url + "todos/" + user_id).json()

    print(type(task_list))
    # get todos json for tasks list
    tasks_done = []
    tasks_total = 0
    todo = requests.get(url + "todos").json()

    # write CSV
    #with open(e_id + ".csv", "w") as file:
