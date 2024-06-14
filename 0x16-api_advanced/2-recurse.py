#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.hot.posts:v1.0 (by /u/elmostafatrade)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                hot_list.append(post["data"]["title"])
            after = data["data"]["after"]
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
