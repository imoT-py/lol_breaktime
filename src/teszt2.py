from responses import response_data

url = f"https://europe.api.riotgames.com/lol/match/v5/matches/EUW1_7470392710"
response = response_data(url, None)
print("match data", response.status_code)

data = response.json()
info = []

max_user = 0

team = data["info"]["teams"][0]['teamId']
puuid = data['info']['participants'][0]['win']
print(puuid)




#EUW1_7454118939 - arena