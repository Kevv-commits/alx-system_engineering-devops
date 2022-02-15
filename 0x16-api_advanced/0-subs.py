#!/usr/bin/python3
"""func that queries the Reddit API."""
import requests

def number_of_subscribers(subreddit):
    """returns the num of subs for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},
                            allow_redirects=False)
    if response.status_code == 200:
        users = response.json().get('data')
        return users.get('subscribers')
    return 0
