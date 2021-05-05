import requests
from .repo import Repo


def fetch_repos(username):
    URL = formatURL(username)
    print(URL)
    req = requests.get(URL)
    for data in req.json():
        Repo(data)
    return data

def formatURL(username): 
    return f'https://api.github.com/users/{username}/repos'

  