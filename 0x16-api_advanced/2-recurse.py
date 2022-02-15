#!/usr/bin/python3
"""Recurse func"""
import requests

def recurse(subreddit, hot_list=[], pagination=""):
    """func which queries the Reddit API & returns a list
    containing the titles of all hot articles for a given subreddit. If no
    res are found, the func should return None
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/' + subreddit +\
          '/hot.json?after={}'.format(pagination)
    r_u = requests.get(url, headers=headers, allow_redirects=False)
    if r_u.status_code != 200:
        return None
    res = r_u.json()
    hot = res.get('data').get('children')
    for pos in hot:
        hot_list.append(pos.get('data').get('title'))
    pagination = res.get('data').get('after')
    if pagination is not None:
        recurse(subreddit, hot_list, pagination)
    return hot_list
