from matches import matches
from users_rank import users_rank
from match_info import match_info
from user_file import user_file


def process(puuids, rank, tier):
    
    for user_id in puuids:
        print("process for:", user_id)
        # copy user_id, rank, tier to users.txt
        users_rank(user_id, rank, tier)
        # get match ids
        match_ids = matches(user_id)
        print("get match_ids")
        # get match info from matches then copy to file
        for match in match_ids:
            info = match_info(match, user_id)
            if info is None:
                continue
            user_file(info, user_id, rank)
