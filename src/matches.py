import requests
from api import headers

data = []

for start in range(0, 500, 100):
    response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/VfsPsngth6fAyuEvLRcQlEZwWjoB5lZxAQvxiSlpamjH5XhXuiJ0nJz4qD7CuXzrkl0XqCW6c16bLQ/ids",params={
        "start": {start},
        "count": 100
        }, headers=headers)
    print("puuids chall", response.status_code)

    data.extend(response.json())
    
print(data)

