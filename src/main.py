import time
from create_folder import folder_file
from puuids import get_puuids_challengers

# 2. Get the user_ids
# 3. Get the their rank -> to user_list.txt // máshogy: adott lekérésben vagyunk, tudjuk rank, tier-t -> az alapján mentünk
# 4. Get their match info

# create outputs folder and users.txt file
folder_file()

# get the 'challengers' data
puuids = get_puuids_challengers()
print(len(puuids))
#process(puuids, 100, 'challenger')