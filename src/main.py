import time
from create_folder import folder_file
from puuids import get_puuids_challengers
from process import process

# 2. Get the user_ids OK
# 3. Get the their rank -> to user_list.txt // máshogy: adott lekérésben vagyunk, tudjuk rank, tier-t -> az alapján mentünk
# 4. Get their match info

# create outputs folder and users.txt file
folder_file()

# get the 'challengers' data
url = "https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
puuids = get_puuids_challengers(url)
print(len(puuids))
process(puuids, "challenger", 1)