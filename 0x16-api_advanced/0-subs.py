#!/usr/bin/python3
"""Module `0-subs`"""


def number_of_subscribers(subreddit):
    """Queries and returns the number of subscribers"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    sub_info = requests.get((url),
                            headers={"User-Agent": "My User_Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0
    return sub_info.json().get("data").get("subscribers")
