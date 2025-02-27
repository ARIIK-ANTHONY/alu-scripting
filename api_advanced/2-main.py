#!/usr/bin/python3
"""
2-main
"""
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse  # Import the recurse function
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])  # Call recurse with the subreddit argument
        if result is not None:
            print(len(result))  # Print the number of posts if the result is valid
        else:
            print("None")  # Print None if the result is invalid or subreddit is not found
