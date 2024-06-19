#!/usr/bin/python3
"""2. Recurse it!(Task 2)"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries the first 10 'hot' posts
    from the Reddit API
    using !!!RECURSION!!!
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={"User_Agent": "sofi_vm"},
                            params={"after": after, "limit": 100},
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    # parse and add titles to list
    post_list = response.json()["data"]["children"]
    for post in post_list:
        hot_list.append(post.get("data").get("title"))

    # check if there are no more items to retrieve
    after = response.json().get("data").get("after")
    # call function with after parameter
    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
