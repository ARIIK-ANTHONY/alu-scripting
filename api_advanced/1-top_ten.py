#!/usr/bin/python3
"""
Reddit Top 10 Posts Fetcher

This module defines a function `top_ten` that fetches and prints the titles of
the first 10 hot posts for a given subreddit using the Reddit API.

If the subreddit is invalid, it prints `None`.

The function does not follow redirects, to avoid being redirected to search
results for non-existent subreddits.

Usage:
    top_ten('programming')

Author: Your Name
"""

import requests


def top_ten(subreddit):
    """
    Fetch and print the top 10 hot post titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Prints:
        - Titles of the top 10 hot posts (one per line).
        - `None` if the subreddit is invalid or does not exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'MyRedditAPI/1.0 (by ALU Student)'
    }
    params = {
        'limit': 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False  # Important to prevent redirect to search page
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children:
            print(None)
            return

        for post in children:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)
