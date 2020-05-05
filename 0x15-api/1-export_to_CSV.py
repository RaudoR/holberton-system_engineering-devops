#!/usr/bin/python3
'''run Emp ID and return TODO list form REST API'''

if __name__ == "__main__":
    import csv
    import json
    import requests as re
    from sys import argv

    userId = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    user = re.get(url + '/{}'.format(userId)).json()
    todo = re.get(url + '/{}/todos'.format(userId)).json()

    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        fil = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            fil.writerow([userId,
                          user.get('username'),
                          task.get('completed'),
                          task.get('title')])
