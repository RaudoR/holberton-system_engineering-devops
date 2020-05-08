#!/usr/bin/python3
'''
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
'''

from requests import get


def recurse(subreddit, hot_list=[], after=""):

    headers = {'User-Agent': 'yook00627'}
    json = get('https://api.reddit.com/r/{}/hot?after={}'.
               format(subreddit, after), headers=headers).json()
    try:
        key = json['data']['after']
        parent = json['data']['children']
        for obj in parent:
            hot_list.append(obj['data']['title'])
        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    except Exception:
        return None
