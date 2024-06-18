#!/usr/bin/python3
"""1.Top Ten(Task 1)"""

import requests


def top_ten(subreddit):
    """queries the first 10 'hot' posts
    from the Reddit API
    """
    url = "https://reddit.com/r/" + subreddit + "/hot.json"
    response = requests.get(url)
    print(response.status_code)
    if (response.status_code == 301 or 302):
        return
    elif response.status_code == 200:
        print(response.json())
        post_list = response.json()['chldren']
        count = 0
        for post in post_list and count < 10:
            print(post['data']['title'])
            count += 1
