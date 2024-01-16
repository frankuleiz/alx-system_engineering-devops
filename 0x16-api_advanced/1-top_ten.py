#!/usr/bin/python3
"""Module `1-top_ten`"""


def top_ten(subreddit):
    """
    Returns the top 10 posts from a given subreddit
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    sub_info = requests.get((url),
                            headers={"User-Agent": "My-User_Agent"},
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        print("None")
    else:
        [print(child.get("data").get("title"))
            for child in sub_info.json().get("data").get("children")]
