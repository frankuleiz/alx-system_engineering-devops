#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import json
import requests


def number_of_subscribers(subreddit):
    """the module subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
