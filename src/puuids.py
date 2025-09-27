import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError
from responses import response_data

def get_puuids_challengers(url):    
    
    response = response_data(url)
             
    data = response.json()
    challengers = data['entries']

    list_puuids = []

    for challenger in challengers:
        puuid_data = challenger['puuid']
        list_puuids.append(puuid_data)
            
    return list_puuids