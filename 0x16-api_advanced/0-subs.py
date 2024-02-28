#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
        return number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # get user agent
    # https://stackoverflow.com/questions/10606133/ -->
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, headers=headers).json()
    subscribers = r.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
