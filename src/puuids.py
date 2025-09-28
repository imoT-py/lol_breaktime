import requests
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError
from responses import response_data

# get user_ids for high elo
def get_puuids(rank):    
    
    url = f"https://euw1.api.riotgames.com/lol/league/v4/{rank}leagues/by-queue/RANKED_SOLO_5x5"
    response = response_data(url, None)
    print("get_puuids")         
    data = response.json()
    users = data['entries']

    list_puuids = []

    for user in users:
        puuid_data = user['puuid']
        list_puuids.append(puuid_data)
            
    return list_puuids

# get user_ids for low elo
def get_puuids_low(rank, tier):
    
    WAIT_TIME = 0.5
    
    list_puuids = []
    
    for page in range(1, 51):
        
        url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{rank}/{tier}?page={page}"
        response = response_data(url, None)
        print("get_puuids_low")
        data = response.json()
        
        for user in data:
            inner_data = user['puuid']
            list_puuids.append(inner_data)
        time.sleep(WAIT_TIME)
        
    return list_puuids