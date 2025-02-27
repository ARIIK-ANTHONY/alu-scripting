#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Return the top 10 hot posts for a given subreddit."""
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
    top_ten("python")
