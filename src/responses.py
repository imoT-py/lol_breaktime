import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError


def response_challengers():      
    
    while True:
        try:
            response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5", headers=headers)
            print("puuids chall", response.status_code)
            
            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(15)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError')
            print(e)
            print("IncompleteRead")
            time.sleep(2)
            continue                

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(2)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(2)
            continue              