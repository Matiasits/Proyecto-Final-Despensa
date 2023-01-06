import requests

def anime():
    url = 'https://api.jikan.moe/v4/top/anime'
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
    return data['data']