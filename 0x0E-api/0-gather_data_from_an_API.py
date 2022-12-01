#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her to-do list progress
"""
import sys
import requests

if __name__ == "__main__":
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    userId = int(sys.argv[1])
    employee_id = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    )
    EMPLOYEE_NAME = employee_id.json().get("name")
    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos")

    for k in todo_list.json():
        if k.get('userId') is id:
            all += 1
        if k.get('userId') is id and k.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    )

    for k in todo_list.json():
        if k.get('userId') is id and k.get('completed') is True:
            print("\t {}".format(k.get('title')))
