from pathlib import Path
import os

def user_file(info, user_id, rank):
    
    directory_path = Path(__file__).resolve().parent.parent
    data_path = directory_path / 'outputs'
    number_files = len(os.listdir(data_path))
    
        
    with open(str(data_path) + "/" + user_id + ".txt", "a+") as file:
        for data in info:
            print(str(data), end=" ", file=file)
    with open(str(data_path) + "/" + user_id + ".txt", "a+") as file:        
        print(file=file)