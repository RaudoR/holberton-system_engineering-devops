#!/usr/bin/python3
'''
function that queries the Reddit API and returns the number of subscribers
'''

import requests as re


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {'User-Agent': 'me'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = re.get(url, headers=headers).json()
    try:
        return (data.get('data').get('subscribers'))
    except:
        return 0
