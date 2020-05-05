#!/usr/bin/python3
'''script to get Emp ID and TODO list from REST API'''

if __name__ == "__main__":
    import requests as re
    from sys import argv

    userId = argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user = re.get(url + '/{}'.format(userId)).json()
    todo = re.get(url + '/{}/todos'.format(userId)).json()
    complete = []

    for task in todo:
        if task.get('completed') is True:
            complete.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format
          (user.get('name'), len(complete), len(todo)))
    for task in complete:
        print('\t {}'.format(task))
