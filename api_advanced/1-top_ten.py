#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests

def top_ten(subreddit):
    """Return the top 10 hot posts for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return
        for i, post in enumerate(posts[:10]):
            print(post.get('data', {}).get('title'))
    else:
        print(None)

# Example usage:
if __name__ == "__main__":
    top_ten("python")
