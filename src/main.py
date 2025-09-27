import time
from create_folder import folder_file
from puuids import get_puuids
from process import process
from puuids import get_puuids_low

# 2. Get the user_ids OK
# 3. Get the their rank -> to user_list.txt // máshogy: adott lekérésben vagyunk, tudjuk rank, tier-t -> az alapján mentünk
# 4. Get their match info

# create outputs folder and users.txt file
folder_file()

rank_list = ['challenger', 'grandmaster', 'master']

for rank in rank_list:
    puuids = get_puuids(rank)
    process(puuids, rank, 'na')

low_elo = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"]
tiers = ["I", "II", "III", "IV"]

for rank in low_elo:
        for tier in tiers:
            puuids = get_puuids_low(rank, tier)
            process(puuids, rank, tier)       
            

# hibamentes futás -> error prone try, except!
# még egyszerűsités?
# kimaxolni az api limiteket, a lehető leggyorsabb mentés!