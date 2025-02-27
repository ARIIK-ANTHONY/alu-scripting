#!/usr/bin/python3
"""
Reddit Top 10 Posts Fetcher

This module defines a function `top_ten` that fetches and prints the titles of the top 10 hot posts
for a given subreddit using Reddit's public API.

If the subreddit does not exist or is inaccessible, the function prints `None` followed by `OK`.

Requirements:
- Python 3
- requests module (install with `pip install requests` if needed)

Usage:
- Call `top_ten(subreddit)` with the name of the subreddit as a string.
- Example: `top_ten('python')`

The output will be:
- Titles of the top 10 hot posts for the subreddit (one per line), followed by `OK`.
- If the subreddit does not exist, `None` is printed, followed by `OK`.


import requests

def top_ten(subreddit):
    """
    Fetch and print the top 10 hot post titles for a given subreddit.
    
    Prints:
        - Titles of the top 10 hot posts.
        - If subreddit is invalid, prints `None`.
        - Always ends with `OK`.

    Args:
        subreddit (str): The name of the subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            print("OK")
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        count = 0
        for post in posts:
            if count >= 10:
                break
            print(post.get('data', {}).get('title'))
            count += 1

        if count == 0:  # In case there are no posts at all.
            print(None)

    except (requests.RequestException, ValueError, KeyError):
        print(None)

    print("OK")
