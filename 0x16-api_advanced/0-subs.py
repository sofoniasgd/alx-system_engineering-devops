#!/usr/bin/python3
"""0. How many subs?(Task 0)"""

import requests


def number_of_subscribers(subreddit):
    """queries the number of subscribers
    (not active users, total subscribers)
    from the Reddit API
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User_Agent': 'sofi_vm'},
                            allow_redirects=False)
    if response.status_code == 200:
        # print(response.json())
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
