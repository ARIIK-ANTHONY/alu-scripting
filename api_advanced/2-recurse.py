#!/usr/bin/python3
"""
2. Recurse it!
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursive function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results are found
    for the given subreddit, the function should return None.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): A list to accumulate the hot post titles (default is an empty list).

    Returns:
        list: A list of hot post titles.
        None: If the subreddit is invalid or there are no posts.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100\
                Safari/537.36'}
    params = {'limit': 100}  # Fetching 100 posts per request to cover pagination

    # Send the GET request to Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # If the subreddit does not exist or is invalid, return None
    if response.status_code == 404:
        return None

    # Parse the response to get the list of posts
    data = response.json().get('data', {})
    children = data.get('children', [])
    
    # Append the titles of the posts to the hot_list
    for child in children:
        hot_list.append(child.get('data', {}).get('title'))

    # Get the next page's "after" value for pagination
    after = data.get('after')

    # If there is no "after" value, we've reached the last page, so return the hot_list
    if after is None:
        return hot_list

    # If there is a next page, recursively call the function to fetch more posts
    params['after'] = after
    return recurse(subreddit, hot_list)
