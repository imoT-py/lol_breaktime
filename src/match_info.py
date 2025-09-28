import requests
from api import headers
from responses import response_data
from maximum_user import maximum_user
from datetime import datetime, timezone

def match_info(match, user_id):

    # get match data from api
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match}"
    response = response_data(url, None)
    print("match_info", response.status_code)

    data = response.json()

    info = []

    # get teamId, match result, lane, championName, gameVersion, game start date, game end date, gameDuration, queueId, match Id, user_id
    for i in range(0, maximum_user(data)):
        puuid = data['info']['participants'][i]['puuid']
        
        if user_id == puuid:
            team_id = data['info']['participants'][i]['teamId']
            info.append(data['info']['participants'][i]['teamId'])
            info.append(data['info']['participants'][i]['win'])
            info.append(data['info']['participants'][i]['lane'])
            info.append(data['info']['participants'][i]['championName'])
            info.append(data['info']['gameVersion'])
            gameCreation = data['info']['gameCreation'] / 1000
            date_gameCreation = datetime.fromtimestamp(gameCreation, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            info.append(date_gameCreation)
            gameEndTimeStamp = data['info']['gameEndTimestamp'] / 1000
            date_gameEndTimeStamp = datetime.fromtimestamp(gameEndTimeStamp, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            info.append(date_gameEndTimeStamp)
            info.append(data['info']['gameDuration'])
            info.append(data['info']['queueId'])
            info.append(match)
            info.append(user_id)

    return info