#!/usr/bin/python3
"""Module `1-top_ten`"""


def top_ten(subreddit):
    """
    Returns the top 10 posts from a given subreddit
    """
    import json
    import requests

    # Update the User-Agent to a unique and descriptive value
    headers = {"User-Agent": "1-top_ten/1.0"}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    sub_info = requests.get(url, headers=headers, allow_redirects=False)

    if sub_info.status_code >= 300:
        print("None")
    else:
        try:
            data = sub_info.json()
            [print(child.get("data").get("title"))
             for child in data.get("data", {}).get("children", [])]
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON response")
