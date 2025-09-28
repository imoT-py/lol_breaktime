from responses import response_data

url = f"https://europe.api.riotgames.com/lol/match/v5/matches/EUW1_7462203319"
response = response_data(url, None)
print("match_info", response.status_code)

data = response.json()

team_pos = data['info']['participants'][0].get('teamPosition')
print(team_pos if team_pos else "None")
    
    
#EUW1_7501536279
#EUW1_7462203319