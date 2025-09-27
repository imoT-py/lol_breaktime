import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError


def response_data(url):      
    
    WAIT_ERROR = 0.5
    WAIT_STATUS = 15
    
    while True:
        try:
            response = requests.get(url, headers=headers)
            print("puuids", response.status_code)
            
            if response.status_code in {429, 500, 502, 503, 504}:
                print("Waiting for the API")
                time.sleep(WAIT_STATUS)
                continue
                
            return response

        except (IncompleteRead, ChunkedEncodingError, ConnectionError) as e:
            print('IncompleteRead, ChunkedEncodingError, ConnectionError', e)
            time.sleep(WAIT_ERROR)
            continue                

        except HTTPError as e:
            print("HTTTPError", e)
            time.sleep(WAIT_ERROR)
            continue
            
        except Exception as e:
            print("Exception", e)
            time.sleep(WAIT_ERROR)
            continue              
        
