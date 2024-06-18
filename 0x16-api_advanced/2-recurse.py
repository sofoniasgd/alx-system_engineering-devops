#!/usr/bin/python3
"""2. Recurse it!(Task 2)"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries the first 10 'hot' posts
    from the Reddit API
    using !!!RECURSION!!!
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "":
        params['after'] = after
    else:
        params = {}
    response = requests.get(url, headers={'User_Agent': 'sofi_vm'},
                            params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        # check if there are no more items to retrieve
        if {response.json()['data']['after'] == None}:
            return

        # parse and add titles to list
        post_list = response.json()['data']['children']
        for post in post_list:
            hot_list.append(post['data']['title'])
        # call function with after parameter
        print("before next call=", len(hot_list))
        recurse(subreddit, hot_list, response.json()['data']['after'])
    else:
        print("None")
        exit()
