#!/usr/bin/python3
"""
export data in the CSV format
"""

import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]

    employee_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
    )
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(USER_ID)
    )
    user_info = json.loads(employee_id.text)
    todo_info = json.loads(todo_list.text)

    tasks = {}
    task_list = []
    for task in todo_info:
        dictionary = {
            'task': task['title'],
            'completed': task['completed'],
            'username': user_info['username']
        }
        task_list.append(dictionary)

    tasks[USER_ID] = task_list

    with open('./{}.json'.format(USER_ID), 'w', encoding='UTF8',
              newline='') as f:
        f.write(json.dumps(tasks))
