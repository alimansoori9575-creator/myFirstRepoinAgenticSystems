import requests

params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": "5"
}

responce = requests.get("https://api.github.com/search/repositories", params=params)

data = responce.json()

items = data['items']

for repo in items:
    print(repo['name'])
    print(repo['stargazers_count'])
