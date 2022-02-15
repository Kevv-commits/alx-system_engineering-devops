#!/usr/bin/python3
"""
func that queries the Reddit API & prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    func queries Reddit API & prints the titles of
    the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},
                            allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            hot = response.json()['data']['children'][i]['data']['title']
            print(hot)
    print("None")
