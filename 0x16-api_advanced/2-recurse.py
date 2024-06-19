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
        response = requests.get(url, headers={'User_Agent': 'sofi_vm'},
                                params={"after": after},
                                allow_redirects=False)
    else:
        response = requests.get(url, headers={'User_Agent': 'sofi_vm'},
                                allow_redirects=False)
    if response.status_code == 200:

        # parse and add titles to list
        post_list = response.json()['data']['children']
        # print(response.status_code)
        for post in post_list:
            hot_list.append(post['data']['title'])
        # check if there are no more items to retrieve
        after = response.json()['data']['after']
        if after is None:
            return hot_list
        # call function with after parameter
        recurse(subreddit, hot_list, after)
        return hot_list
    else:
        exit()
