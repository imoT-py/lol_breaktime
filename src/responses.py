import requests
from api import headers
import time
from http.client import IncompleteRead
from requests.exceptions import ChunkedEncodingError, ConnectionError, HTTPError

# make api call to get info
def response_data(url, params):      
    
    WAIT_ERROR = 0.5
    
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            print("response_data", response.status_code)
            
            # check the api limit
            limit = response.headers.get("X-App-Rate-Limit")
            count = response.headers.get("X-App-Rate-Limit-Count")
            print(">>>>>", limit, count)
            if response.status_code in {429, 500, 502, 503, 504}:
                # give how much time need to wait
                retry_after = int(response.headers.get("Retry-After", 1))
                print(retry_after)
                print("Waiting for the API")
                time.sleep(retry_after)
                continue
                
            elif response.status_code == 404:
                print("404 Not Found:", url)
                return None
            
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
        

