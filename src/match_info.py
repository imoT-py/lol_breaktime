import requests
from api import headers
from responses import response_data

def match_info(match, user_id):

    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match}"
    response = response_data(url, None)
    print("match data", response.status_code)

    data = response.json()

    info = []

    for i in range(0, 10):
        puuid = data['info']['participants'][i]['puuid']
        
        if user_id == puuid:
            team_id = data['info']['participants'][i]['teamId']
            info.append(data['info']['participants'][i]['teamId'])
            
            for j in range(0, 2):
                team = data["info"]["teams"][j]['teamId']
                if team_id == team:
                    info.append(data["info"]["teams"][j]['win'])

            info.append(data['info']['participants'][i]['lane'])
            info.append(data['info']['participants'][i]['championName'])
            info.append(data['info']['gameVersion'])
            info.append(data['info']['gameCreation'])
            info.append(data['info']['gameEndTimestamp'])
            info.append(data['info']['gameDuration'])
            info.append(data['info']['queueId'])
            info.append(match)

    return info