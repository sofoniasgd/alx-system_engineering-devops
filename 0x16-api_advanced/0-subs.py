#!/usr/bin/python3
"""0. How many subs?(Task 0)"""

import requests


def number_of_subscribers(subreddit):
    """queries the number of subscribers
    (not active users, total subscribers)
    from the Reddit API
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'user_agent': 'custom'},
                            allow_redirects=False)
    if (response.status_code == 200):
        # print(response.json())
        data = response.json()
        subscriber_number = data['data']['subscribers']
        return subscriber_number
    else:
        return 0
