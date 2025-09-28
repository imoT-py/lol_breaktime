from pathlib import Path

# save user_id, rank, tier to users.txt
def users_rank(user_id, rank, tier):
    
    directory_path = Path(__file__).resolve().parent.parent
    data_path = directory_path / 'outputs'
        
    with open(str(data_path) + "/" + "users.txt", "a") as file:
        file.write(user_id + ' ' + rank + ' ' + str(tier) + '\n')
        
    print("Saved to users.txt")