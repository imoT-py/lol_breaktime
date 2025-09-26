import requests
from api import headers


response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/EUW1_7480186572", headers=headers)
print("match data", response.status_code)

data = response.json()
user = 'bHDZewXhRaH-W71CgczzoA3XmsifIfqKDS3ZGfK_6ukS8CAyOOik3ugRH_4OcP3cS59kjnwLzVrlkA'

li = []

for i in range(0, 10):
    puuid = data['info']['participants'][i]['puuid']
    
    if user == puuid:
        team_id = data['info']['participants'][i]['teamId']
        li.append(data['info']['participants'][i]['teamId'])
        li.append(data['info']['participants'][i]['lane'])
        li.append(data['info']['participants'][i]['championName'])
        li.append(data['info']['gameVersion'])

        for j in range(0, 2):
            team = data["info"]["teams"][j]['teamId']
            if team_id == team:
                li.append(data["info"]["teams"][j]['win'])
    # print(puuid)
print(li)

game_start_timestamp = data['info']['gameCreation']
game_end_timestamp = data['info']['gameEndTimestamp']
game_duration = data['info']['gameDuration']
match_type = data['info']['queueId']
print(game_start_timestamp)
print(game_end_timestamp)
print(game_duration)
print(match_type)

response2 = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{user}", headers=headers) 
data2 = response2.json()

rank = data2[0]['tier']
tier = data2[0]['rank']

print(rank)
print(tier)