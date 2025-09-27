from matches import matches
from users_rank import users_rank
from match_info import match_info

def process(puuids, rank, tier):
    
    for user_id in puuids:
        
        users_rank(user_id, rank, tier)
        match_ids = matches(user_id)
        
        for match in match_ids:
            info = match_info(match, user_id)
            
            print(info)