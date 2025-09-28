from create_folder import folder_file
from puuids import get_puuids, get_puuids_low
from process import process


# create outputs folder and users.txt file
folder_file()

high_elo = ['challenger', 'grandmaster', 'master']

# get users, users' match data from high elo
for rank in high_elo:
    print("saving high elo matches has been started:", rank)
    puuids = get_puuids(rank)
    print("puuids saved, continue with process...", rank)
    process(puuids, rank, 'na')
    print("process completed for:", rank)

low_elo = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"]
tiers = ["I", "II", "III", "IV"]

# get users, users' match data from low elo
for rank in low_elo:
        for tier in tiers:
            print("saving low elo matches has been started:", rank, tier)
            puuids = get_puuids_low(rank, tier)
            print("puuids saved, continue with process...", rank, tier)
            process(puuids, rank, tier)       
            print("process completed for:", rank, tier)

# hibamentes futás -> error prone try, except!
# még egyszerűsités?
# kimaxolni az api limiteket, a lehető leggyorsabb mentés!
# time.sleep(1.2)  # API rate limit védelem (kb. 50 request/perc)