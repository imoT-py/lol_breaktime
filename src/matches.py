import requests
from api import headers
from responses import response_data


def matches(user_id):

    data = []

    for matches in range(0, 500, 100):
        url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{user_id}/ids"
        params={
            "start": matches,
            "count": 100}
        
        response = response_data(url, params)
        data.extend(response.json())

    data = list(set(data)) 
    print(len(data))   

    return data