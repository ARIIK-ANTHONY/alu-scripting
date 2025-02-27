#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Fetch and print titles of the top 10 hot posts for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        print("OK")
        return

    try:
        data = response.json().get('data', {})
        posts = data.get('children', [])

        for post in posts[:10]:
            print(post.get('data', {}).get('title'))

    except (KeyError, IndexError, ValueError):
        print(None)

    print("OK")
