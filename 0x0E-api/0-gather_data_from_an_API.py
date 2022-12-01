#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her to-do list progress
"""

import json
import sys
from urllib import request


if __name__ == "__main__":

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    todos_req = request.Request('https://jsonplaceholder.typicode.com/todos')
    users_req = request.Request('https://jsonplaceholder.typicode.com/users')

    with request.urlopen(todos_req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for x in data:
            if x.get('userId') == int(sys.argv[1]):
                TOTAL_NUMBER_OF_TASKS += 1
                if x.get('completed') is True:
                    NUMBER_OF_DONE_TASKS += 1

    with request.urlopen(users_req) as resu:
        data = json.loads(resu.read().decode('utf-8'))
        for k in data:
            if k.get('id') == int(sys.argv[1]):
                EMPLOYEE_NAME = k['name']

    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    with request.urlopen(todos_req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for x in data:
            if x.get('userId') == int(sys.argv[1]):
                if x.get('completed') is True:
                    print('\t {}'.format(x['title']))
