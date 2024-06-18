#!/usr/bin/python3
"""0. How many subs?(Task 0)"""

import requests


def number_of_subscribers(subreddit):
    """queries the number of subscribers
    (not active users, total subscribers)
    from the Reddit API
    """
    url = "https://reddit.com/r/" + subreddit + "/about.json"
    response = requests.get(url, allow_redirects=False)
    # print(response.status_code)
    if (response.status_code == 301 or 302):
        return 0
    elif response.status_code == 200:
        # print(response.json())
        data = response.json()
        subscriber_number = data['data']['subscribers']
        return subscriber_number
