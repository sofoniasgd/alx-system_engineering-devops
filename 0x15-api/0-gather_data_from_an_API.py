#!/usr/bin/python3
"""0. Gather data from an API
displays employee tasks data"""


import requests
import sys

if __name__ == "__main__":
    """ Display completed tasks by an employee
    display format:
    Employee "EMPLOYEE_NAME" is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        completed task 1
        completed task 2
        ...
    """
    url = "https://jsonplaceholder.typicode.com/"
    e_id = sys.argv[1]

    employee_name = requests.get(url + "users/" + e_id).json()["name"]

    # get todos json for tasks list
    tasks_done = []
    tasks_total = 0
    todo = requests.get(url + "todos").json()
    for task in todo:
        if task['userId'] == int(e_id):
            tasks_total += 1
            if task["completed"]:
                tasks_done.append(task["title"])

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, len(tasks_done), tasks_total))
    for task in tasks_done:
        print("\t", task)
