#!/usr/bin/python3
"""Script that fetches the top 10 hot posts from a given subreddit.

This script interacts with the Reddit API to retrieve and display the titles
of the top 10 hot posts for a specified subreddit. If the subreddit does not
exist or an error occurs, the script will output `None`.

Usage:
    ./1-top_ten.py <subreddit>

Example:
    ./1-top_ten.py python

    Output:
    Title of post 1
    Title of post 2
    ...
    Title of post 10

Requirements:
    - Python 3.x
    - `requests` library (install via `pip install requests`)

Functions:
    top_ten(subreddit):
        Fetches and prints the titles of the top 10 hot posts for a given subreddit.

        Args:
            subreddit (str): The name of the subreddit to fetch posts from.

        Returns:
            None: Outputs the titles directly to the console or `None` if an error occurs.
"""

import requests


def top_ten(subreddit):
    """Return the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch posts from.

    Returns:
        None: Outputs the titles directly to the console or `None` if an error occurs.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            json_data = response.json()
            posts = json_data.get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
        except ValueError:
            print(None)
    else:
        print(None)


# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: ./1-top_ten.py <subreddit>")
    else:
        top_ten(sys.argv[1])
