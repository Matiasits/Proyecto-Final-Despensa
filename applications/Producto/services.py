import requests

def get_nbaTeams():
    url = "https://free-nba.p.rapidapi.com/teams"

    querystring = {"page":"0"}

    headers = {
        "X-RapidAPI-Key": "9368d90876msh7b4b8ff318aa150p1f5190jsne14ca3b76345",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    teams = response.json()

    teamData = teams['data']    
    teamList = [ i for i in teamData ]
    
    return teamList

def get_gamesFree():
    
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"

    headers = {
        "X-RapidAPI-Key": "9368d90876msh7b4b8ff318aa150p1f5190jsne14ca3b76345",
        "X-RapidAPI-Host": "free-to-play-games-database.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    freeGames = response.json()
    
    gamesList = []
    counter = 0
    while counter < 10:
        game = freeGames[counter]
        gamesList.append(game['title'])
        counter += 1
        
    return gamesList

print(get_gamesFree())
    
     
    