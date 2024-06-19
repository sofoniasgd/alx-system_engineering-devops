#!/usr/bin/python3
"""1.Top Ten(Task 1)"""

import requests


def top_ten(subreddit):
    """queries the first 10 'hot' posts
    from the Reddit API
    """
    if subreddit is None or type(subreddit) is not str:
        print("None")
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={"User_Agent": "sofi_vm"},
                            params={"limit": 10},
                            allow_redirects=False)
    if response.status_code == 200:
        post_list = response.json()["data"]["children"]
        for post in post_list:
            print(post["data"]["title"])
    else:
        print("None")
        return
