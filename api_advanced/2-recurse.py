#!/usr/bin/python3
"""
2. Recurse it!
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ 
    Function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results
    are found for the given subreddit, the function should return None.
    The function is recursive and keeps calling itself until all posts 
    are retrieved.
    """
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100\
                Safari/537.36'}
    params = {'limit': 100, 'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    
    # Send GET request to Reddit API
    res = requests.get(url, headers=headers, params=params)
    
    # If subreddit does not exist (404), return None
    if res.status_code == 404:
        return None
    
    # Parse the response to get the list of hot posts
    children = res.json().get('data', {}).get('children', [])
    
    # Append the titles of the posts to hot_list
    for child in children:
        hot_list.append(child.get('data', {}).get('title'))
    
    # Check if there is a next set of posts (pagination)
    after = res.json().get('data', {}).get('after')
    
    # If there is no "after", we have reached the end of the posts
    if after is None:
        return hot_list
    
    # Otherwise, recurse to fetch the next set of posts
    return recurse(subreddit, hot_list, after)
