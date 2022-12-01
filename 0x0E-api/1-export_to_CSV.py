#!/usr/bin/python3
"""
export data in the CSV format
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    USER_ID = sys.argv[1]

    employee_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
    )
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(USER_ID)
    )
    user_info = json.loads(employee_id.text)
    todo_info = json.loads(todo_list.text)

    task_list = []
    USERNAME = user_info['username']
    for task in todo_info:
        dictionary = {
            'USER_ID': USER_ID,
            'USERNAME': USERNAME,
            'TASK_COMPLETED_STATUS': task['completed'],
            'TASK_TITLE': task['title']
        }
        task_list.append(dictionary)

    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    with open('./{}.csv'.format(USER_ID), 'w', encoding='UTF8',
              newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(task_list)
